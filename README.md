                 ┌──────────────────┐
                 │   User Uploads   │
                 │ Blood Report TXT │
                 └────────┬─────────┘
                          │
                          ▼
              ┌───────────────────────┐
              │   Streamlit Frontend │
              └───────────┬───────────┘
                          │
                          ▼
          ┌──────────────────────────────┐
          │ Stage 1: Gemini AI Analysis │
          │ Extract Lab Values          │
          │ HIGH / LOW / NORMAL         │
          └──────────────┬───────────────┘
                         │
                         ▼
          ┌──────────────────────────────┐
          │ Stage 2: Gemini AI           │
          │ Health Summary + Diet Plan   │
          └──────────────┬───────────────┘
                         │
                         ▼
                ┌────────────────┐
                │ Streamlit UI   │
                │ Results Display│
                └────────────────┘
