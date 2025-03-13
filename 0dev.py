import requests
ticker="AAPL"
headers={"User-Agent":"MyApp (myemail@example.com)"}
cik_url="https://www.sec.gov/files/company_tickers.json"
cik_response=requests.get(cik_url,headers=headers).json()
ticker_lower=ticker.lower()
cik=None
for entry in cik_response.values():
    if entry["ticker"].lower()==ticker_lower:
        cik=str(entry["cik_str"]).zfill(10)
        break
if not cik:exit()
filings_url=f"https://data.sec.gov/submissions/CIK{cik}.json"
filings_data=requests.get(filings_url,headers=headers).json()
recent_filings=filings_data["filings"]["recent"]
forms=recent_filings["form"]
filing_dates=recent_filings["filingDate"]
eight_k_dates=[date for form,date in zip(forms,filing_dates) if form=="8-K"]
print(",".join(eight_k_dates))
