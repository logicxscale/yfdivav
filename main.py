import os
import glob

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

def get_indonesia_stock_list():
    pattern = os.path.join(os.getcwd(), "downloads", "Daftar Saham  - *.xlsx")
    files = glob.glob(pattern)

    if not files:
        raise FileNotFoundError("No stock files found in the specified directory.")
    
    files.sort(key=os.path.getmtime, reverse=True) 

    return files[0]

def get_yf_data(stock_code):
    try:
        stock = yf.Ticker(stock_code.upper())
        return stock
    except Exception as e:
        raise FileNotFoundError(f"Error fetching data for {stock_code}: {e}")

## Streamlit
isl = pd.read_excel(get_indonesia_stock_list())

@st.dialog("Select Indonesia Stocks List")
def indonesia_stock_list():

    st.write("Please select the latest Indonesia stock list file.")
    try:
        df = isl
        
        event = st.dataframe(df, 
            use_container_width=True,
            on_select="rerun")
        
        selected_rows = df.iloc[event.selection.rows[0]]        
        st.write(selected_rows)

        if st.button("Submit"):
            st.session_state["stock_input"] = ""
            st.session_state["stock"] = selected_rows
            st.success("Stock selected successfully!")
            st.rerun()

    except FileNotFoundError as e:
        st.error(f"Error: {e}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")

@st.dialog("Informations (!)")
def informations():
    st.write("Period is the time range for which you want to retrieve stock data.")    
    st.table(pd.DataFrame({
        "period": [
            "3mo",
            "max",
            "ytd",
            "10y",
            "5y",
            "2y",
            "1y",
            "6mo",
            "1mo",
            "7d",
            "5d",
            "1d"
        ],
        "Meanings of period": [
            "3 bulan terakhir",
            "Semua data historis yang tersedia",
            "Dari awal tahun ini sampai hari ini",
            "10 tahun terakhir",
            "5 tahun terakhir",
            "2 tahun terakhir",
            "1 tahun terakhir",
            "6 bulan terakhir",
            "1 bulan terakhir",
            "7 hari terakhir",
            "5 hari terakhir",
            "1 hari terakhir"
        ]
    }))

def yf_data():
    data = None
    if "stock" in st.session_state:
        data = get_yf_data(st.session_state["stock"]["Kode"])

    if data:
        col1, col2 = st.columns(2)
        with col1: 
            st.subheader("Period")
        with col2:
            if st.button("Informations (!)"):
                informations()
        period = st.text_input("", value="1y")

        st.subheader("History")
        st.line_chart(data.history(period)['Close'])

        st.divider()
        st.subheader("Dividends")
        dividends = data.dividends
        # Tampilkan data dividen jika ada
        if not dividends.empty:
            st.subheader("Riwayat Dividen")
            st.write(dividends)

            # Tampilkan chart dividen
            st.subheader("Grafik Dividen")
            fig, ax = plt.subplots()
            dividends.plot(kind='bar', ax=ax)
            ax.set_ylabel("Dividen per Saham (USD/Rp)")
            ax.set_xlabel("Tanggal")
            ax.set_title("Dividen dari Saham")
            st.pyplot(fig)
        else:
            st.warning("Data dividen tidak tersedia untuk saham ini.")

        if not dividends.empty:
            average_dividend = dividends.mean()
            st.subheader(f"Average Dividend: {average_dividend:.2f} USD/Rp")
        else:
            st.warning("Tidak ada data dividen untuk menghitung rata-rata.")

        if not dividends.empty:
            highest_dividend = dividends.max()
            date_of_highest = dividends.idxmax()
            st.subheader(f"Highest Dividend {date_of_highest.date()}: {highest_dividend:.2f} USD/Rp")
        else:
            st.warning("Tidak ada data dividen untuk menghitung tertinggi.")

        if not dividends.empty:
            total_dividend = dividends.sum()
            st.subheader(f"Total Dividend: {total_dividend:.2f} USD/Rp")
        else:
            st.warning("Tidak ada data dividen untuk menghitung total.")
    else:
        st.warning("No Data Found.")

def main():
    st.set_page_config(layout="wide")

    st.title("Yahoo Finance Dividend Average")

    col1, col2 = st.columns([2, 6])

    with col1:
        st.write("Select Available Indonesia Stocks List.")
        if st.button("Indonesia Stock List"):
            indonesia_stock_list()

        st.write("Or You Can Input Stock Code:")
        stock_input = st.text_input("Stock Code", placeholder="e.g. BBCA.JK", key="stock_input").upper()

        if stock_input:
            st.session_state["stock"] = {"Kode": None}
            if stock_input in isl['Kode'].values:
                st.session_state["stock"]["Kode"] = stock_input + ".JK"
            else:
                st.session_state["stock"]["Kode"] = stock_input

        if 'stock' in st.session_state:
            st.write("Selected Stock:")
            st.write(st.dataframe(get_yf_data(st.session_state["stock"]["Kode"]).info))
        else:
            st.info("Stock not selected.")

    with col2:
        yf_data()

if __name__ == "__main__": 
    main()