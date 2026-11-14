# BNPL Underwriting & Virtual Card Engine

An end-to-end Buy Now, Pay Later (BNPL) underwriting and single-use virtual card issuance prototype built with Python, Plaid, and Google Cloud Platform.

## Architecture & Workflow
1. **Bank Connection (Plaid):** Connects to a user's checking account via Plaid Link to retrieve real-time balances and historical transactions.
2. **Cash-Flow Underwriting (`src/underwriting.py`):** Evaluates monthly income consistency, average daily balance, and NSF/overdraft frequency to output an `APPROVED` (with dollar limit) or `DECLINED` decision.
3. **Single-Use Card Issuance (`src/card_issuer.py`):** Generates a single-use virtual card capped at the approved loan amount (*currently stubbed with a mock placeholder; designed for drop-in Lithic API integration*).
4. **Installment Scheduling (`src/repayments.py`):** Splits the approved principal into a 4-part bi-weekly repayment schedule upon authorization.

## Tech Stack
* **Language & Framework:** Python 3.11+, FastAPI
* **Banking Data:** Plaid API (Sandbox)
* **Card Issuing:** Mock Issuer Placeholder (Target: Lithic API)
* **Cloud & Persistence:** Google Cloud Run, Cloud SQL (PostgreSQL), GCP Secret Manager

## Project Structure
* `src/main.py` — Orchestrates the end-to-end workflow and exposes API endpoints.
* `src/plaid_client.py` — Handles Plaid token exchange and transaction data retrieval.
* `src/underwriting.py` — Core risk-scoring and loan limit calculation functions.
* `src/card_issuer.py` — Virtual card creation and real-time authorization webhook handlers.
* `src/repayments.py` — Repayment schedule generator and ledger tracking.
* `src/database.py` — PostgreSQL connection and CRUD helper functions.

## Build Roadmap
- [x] Map end-to-end process architecture & project structure
- [ ] Build cash-flow underwriting functions (`src/underwriting.py`)
- [ ] Implement mock single-use card issuer (`src/card_issuer.py`)
- [ ] Wire orchestration flow in `src/main.py`
- [ ] Connect Cloud SQL PostgreSQL (`src/database.py`)
- [ ] Containerize with `Dockerfile` and deploy to Cloud Run
- [ ] Swap mock issuer placeholder for Lithic Sandbox API