import random
import time
import sys

# --- REAL-LIFE SYSTEMS SIMULATOR v3 (ULTIMATE SPAGHETTI) ---
# Global variables for real-world metrics, currencies, and systems.

country_name = "CRISPY REPUBLIC"
usd_balance = 25000000.0  # 25 Million USD
eur_balance = 15000000.0  # 15 Million EUR
cny_balance = 50000000.0  # 50 Million CNY
local_currency_balance = 500000000.0
exchange_rate_usd = 3.75  # Local to USD
exchange_rate_eur = 4.00  # Local to EUR
exchange_rate_cny = 0.52  # Local to CNY
inflation_rate = 0.025
gdp = 1000000000.0
population = 2500000
unemployment_rate = 0.055
tax_revenue = 0.0
government_debt = 150000000.0
interest_rate = 0.04
year = 2026
month = 3
is_game_over = False

# Infrastructure & Services
healthcare_quality = 70
education_level = 65
military_strength = 50
infrastructure_index = 60
corruption_index = 10
energy_security = 75
environmental_health = 80

# Political System
political_stability = 90
public_approval = 80
is_democracy = True
last_election_year = 2024
rebellion_risk = 0
international_sanctions = 0 # 0 to 100

# Trade & Global Relations
oil_price = 85.0
gold_price = 2200.0
bitcoin_price = 70000.0
export_volume = 1500000.0
import_volume = 1200000.0
crypto_balance = 0.0
gold_reserve = 10000.0 # oz

# Stock Market
stock_index = 15000.0
is_market_open = True

# Global Events
climate_change_impact = 0.01
global_tension = 20 # 0 to 100

def show_dashboard():
    print("\n" + "═"*90)
    print(f"🏛️  {country_name} - {month}/{year} 🏛️")
    print(f"💵 USD: {usd_balance:,.2f} | 💶 EUR: {eur_balance:,.2f} | 💴 CNY: {cny_balance:,.2f}")
    print(f"💰 Local: {local_currency_balance:,.2f} | 🪙 BTC: {crypto_balance:,.4f} | 🟡 Gold: {gold_reserve:,.2f} oz")
    print(f"📈 GDP: {gdp:,.2f} | 👥 Pop: {population:,} | 💼 Unemp: {unemployment_rate*100:.2f}%")
    print(f"📊 Inflation: {inflation_rate*100:.2f}% | 🏛️  Debt: {government_debt:,.2f} | 📈 Rate: {interest_rate*100:.2f}%")
    print(f"🏥 Health: {healthcare_quality}% | 🎓 Edu: {education_level}% | ⚡ Energy: {energy_security}% | 🌿 Env: {environmental_health}%")
    print(f"⚖️  Stability: {political_stability}% | 👍 Approval: {public_approval}% | 📉 Corruption: {corruption_index}%")
    print(f"📉 Stock Index: {stock_index:,.2f} | 🛢️ Oil: ${oil_price:.2f} | 🟡 Gold Price: ${gold_price:.2f}")
    print(f"🌍 Global Tension: {global_tension}% | 🚫 Sanctions: {international_sanctions}%")
    print("═"*90)

def slow_print(text, speed=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

slow_print("WELCOME TO THE ULTIMATE REAL-WORLD SYSTEMS SIMULATOR: CRISPY BROTHER EDITION", 0.02)
slow_print("The world is interconnected. Your decisions in one sector will echo across the globe.", 0.02)

while not is_game_over:
    show_dashboard()
    
    print("\nSelect Department to Manage:")
    print("1. Central Bank (Currency, Interest Rates, Crypto, Gold, Reserves)")
    print("2. Ministry of Finance (Taxes, Debt, Stock Market, Bonds)")
    print("3. Ministry of Interior (Healthcare, Education, Infrastructure, Energy, Environment)")
    print("4. Ministry of Defense & Foreign Affairs (Military, Trade, Oil, Diplomacy, Sanctions)")
    print("5. Next Month (Simulate Time)")
    print("6. Resign (Quit)")
    
    choice = input("> ")
    
    if choice == "1":
        print("\n--- CENTRAL BANK ---")
        print("a: Adjust Interest Rate, b: Buy/Sell Gold, c: Buy/Sell Bitcoin, d: Currency Exchange (USD/EUR/CNY)")
        cb_choice = input("> ").lower()
        if cb_choice == "a":
            interest_rate = float(input("New Interest Rate (e.g., 0.04): "))
            inflation_rate -= (interest_rate - 0.04) * 0.7
            unemployment_rate += (interest_rate - 0.04) * 0.4
            print(f"Interest rate adjusted to {interest_rate*100}%.")
        elif cb_choice == "b":
            amt = float(input("Amount of Gold to trade (oz, negative to sell): "))
            cost = amt * gold_price
            if usd_balance >= cost:
                usd_balance -= cost; gold_reserve += amt
                print(f"Gold trade completed. Reserve: {gold_reserve:,.2f} oz")
            else:
                print("Insufficient USD reserves.")
        elif cb_choice == "c":
            amt = float(input("Amount of Bitcoin to trade (negative to sell): "))
            cost = amt * bitcoin_price
            if usd_balance >= cost:
                usd_balance -= cost; crypto_balance += amt
                print(f"Bitcoin trade completed. Balance: {crypto_balance:,.4f} BTC")
            else:
                print("Insufficient USD reserves.")
        elif cb_choice == "d":
            print(f"1 USD = {exchange_rate_usd} L | 1 EUR = {exchange_rate_eur} L | 1 CNY = {exchange_rate_cny} L")
            curr = input("Exchange USD, EUR, or CNY? ").upper()
            amt = float(input("Amount to sell for Local Currency: "))
            if curr == "USD" and usd_balance >= amt:
                usd_balance -= amt; local_currency_balance += amt * exchange_rate_usd
            elif curr == "EUR" and eur_balance >= amt:
                eur_balance -= amt; local_currency_balance += amt * exchange_rate_eur
            elif curr == "CNY" and cny_balance >= amt:
                cny_balance -= amt; local_currency_balance += amt * exchange_rate_cny
            else:
                print("Invalid currency or insufficient balance.")

    elif choice == "2":
        print("\n--- FINANCE ---")
        print("a: Set Income Tax, b: Set Corporate Tax, c: Issue Sovereign Bonds, d: Stock Market Intervention")
        f_choice = input("> ").lower()
        if f_choice == "a":
            new_tax = float(input("New Income Tax Rate (e.g., 0.20): "))
            public_approval -= (new_tax - 0.15) * 200
            tax_revenue = gdp * new_tax / 12
            print(f"Income tax set to {new_tax*100}%.")
        elif f_choice == "b":
            corp_tax = float(input("New Corporate Tax Rate (e.g., 0.15): "))
            gdp *= (1 - (corp_tax - 0.10) * 0.6)
            stock_index *= (1 - (corp_tax - 0.10) * 3)
            print(f"Corporate tax set to {corp_tax*100}%.")
        elif f_choice == "c":
            amount = float(input("Amount of sovereign bonds to issue (USD): "))
            usd_balance += amount
            government_debt += amount * 1.20 # 20% interest on sovereign bonds
            print(f"Issued {amount:,.2f} in sovereign bonds.")
        elif f_choice == "d":
            amt = float(input("Amount of USD to inject into Stock Market: "))
            if usd_balance >= amt:
                usd_balance -= amt; stock_index += (amt / 1000000) * 150
                print("Market intervention successful.")

    elif choice == "3":
        print("\n--- INTERIOR ---")
        print("a: Healthcare (5M USD), b: Education (5M USD), c: Infrastructure (10M USD), d: Energy Security (5M USD), e: Environmental Protection (5M USD)")
        i_choice = input("> ").lower()
        if i_choice == "a" and usd_balance >= 5000000:
            usd_balance -= 5000000; healthcare_quality += 10; public_approval += 7
        elif i_choice == "b" and usd_balance >= 5000000:
            usd_balance -= 5000000; education_level += 10; gdp *= 1.04
        elif i_choice == "c" and usd_balance >= 10000000:
            usd_balance -= 10000000; infrastructure_index += 20; unemployment_rate -= 0.03
        elif i_choice == "d" and usd_balance >= 5000000:
            usd_balance -= 5000000; energy_security += 25; political_stability += 8
        elif i_choice == "e" and usd_balance >= 5000000:
            usd_balance -= 5000000; environmental_health += 15; public_approval += 5

    elif choice == "4":
        print("\n--- DEFENSE & FOREIGN AFFAIRS ---")
        print("a: Military Modernization (20M USD), b: Trade Agreement, c: Sell Oil Reserves, d: Diplomatic Mission (5M USD)")
        d_choice = input("> ").lower()
        if d_choice == "a" and usd_balance >= 20000000:
            usd_balance -= 20000000; military_strength += 30; global_tension += 5
        elif d_choice == "b":
            if political_stability > 80 and international_sanctions < 20:
                export_volume *= 1.20; gdp *= 1.03; print("Trade agreement signed.")
            else:
                print("Stability too low or sanctions too high for agreements.")
        elif d_choice == "c":
            amt = float(input("Barrels of oil to sell: "))
            revenue = amt * oil_price
            usd_balance += revenue
            print(f"Sold oil for {revenue:,.2f} USD.")
        elif d_choice == "d" and usd_balance >= 5000000:
            usd_balance -= 5000000; international_sanctions -= 10; global_tension -= 5
            print("Diplomatic mission successful. Sanctions reduced.")

    elif choice == "5":
        # --- MONTHLY SIMULATION (THE SPAGHETTI CORE v3) ---
        month += 1
        if month > 12:
            month = 1; year += 1
        
        # Economic Calculations
        gdp_growth = (education_level / 1500) + (infrastructure_index / 3000) + (energy_security / 4000) - (inflation_rate / 6) - (international_sanctions / 500)
        gdp *= (1 + gdp_growth)
        
        # Monthly Expenses & Revenue
        maintenance_cost = (healthcare_quality + education_level + military_strength + infrastructure_index + environmental_health) * 50000
        usd_balance -= maintenance_cost
        
        monthly_interest = (government_debt * interest_rate) / 12
        usd_balance -= monthly_interest
        
        # Market Fluctuations
        oil_price += random.uniform(-10, 10)
        gold_price += random.uniform(-100, 100)
        bitcoin_price += random.uniform(-8000, 8000)
        stock_index *= (1 + random.uniform(-0.07, 0.07))
        exchange_rate_usd *= (1 + (inflation_rate / 12))
        
        # Global Tension & Sanctions
        if global_tension > 50:
            international_sanctions += 2; print("Global tensions are rising. Sanctions risk increased.")
        
        # Random Events
        event = random.randint(1, 30)
        if event == 1:
            print("!!! GLOBAL FINANCIAL COLLAPSE !!!")
            stock_index *= 0.6; gdp *= 0.85; usd_balance -= 15000000; international_sanctions += 10
        elif event == 2:
            print("!!! MAJOR OIL SPILL !!!")
            environmental_health -= 25; usd_balance -= 10000000; public_approval -= 15
        elif event == 3:
            print("!!! REVOLUTIONARY TECH BREAKTHROUGH !!!")
            gdp *= 1.15; education_level += 5; stock_index *= 1.2
        elif event == 4:
            print("!!! REGIONAL WAR !!!")
            global_tension += 20; oil_price += 40; export_volume *= 0.7
        elif event == 5:
            print("!!! CLIMATE DISASTER !!!")
            infrastructure_index -= 20; population -= 50000; usd_balance -= 20000000
        
        # Consequences
        if inflation_rate > 0.25:
            public_approval -= 20; political_stability -= 15; print("Hyperinflation is out of control!")
        
        if environmental_health < 40:
            print("ENVIRONMENTAL COLLAPSE! Public health is declining."); healthcare_quality -= 10; public_approval -= 10
            
        if usd_balance < 0:
            print("SOVEREIGN DEFAULT!"); government_debt += abs(usd_balance) * 3; usd_balance = 0; inflation_rate += 0.25; international_sanctions += 30
            
        # Win/Loss Conditions
        if political_stability <= 0:
            print("TOTAL COLLAPSE! The nation has fallen into civil war."); is_game_over = True
        elif gdp < 100000000:
            print("The economy has disintegrated."); is_game_over = True
        elif population <= 0:
            print("The population has vanished."); is_game_over = True

    elif choice == "6":
        print("You have resigned. Your legacy is now in the hands of historians."); is_game_over = True
    
    # Spaghetti logic: Unconnected state management
    if public_approval > 100: public_approval = 100
    if public_approval < 0: public_approval = 0
    if political_stability > 100: political_stability = 100
    if political_stability < 0: political_stability = 0
    if international_sanctions > 100: international_sanctions = 100
    if international_sanctions < 0: international_sanctions = 0
    
    time.sleep(1.5)

print("\n" + "🏛️"*50)
print(f"FINAL GDP: {gdp:,.2f} USD")
print(f"FINAL DEBT: {government_debt:,.2f} USD")
print(f"FINAL POPULATION: {population:,}")
print(f"FINAL APPROVAL: {public_approval}%")
print(f"FINAL SANCTIONS: {international_sanctions}%")
print("🏛️"*50)
