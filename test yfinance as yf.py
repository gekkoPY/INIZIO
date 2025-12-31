import yfinance as yf

print("Tentativo di connessione a Yahoo...")
# Scarichiamo SOLO Apple per testare
test_data = yf.download("AAPL", start="2024-01-01", end="2024-01-10")

print("\n--- RISULTATO ---")
print(test_data.head())