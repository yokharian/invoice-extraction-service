# 🧠 PRD: Invoice Extraction Service

## tl;dr

Automated invoice (CFDI) extraction from SAT using an asynchronous webhook-based pipeline built with FastAPI. The system submits extraction requests to SAT.ws, receives webhook notifications when invoices are ready, and downloads XML/PDF files for downstream processing — supporting 30+ accounts with zero manual intervention.

---

## 🎯 Goals

- **Automated CFDI Extraction**: Eliminate manual invoice retrieval by integrating with SAT.ws cloud API
- **Asynchronous Processing**: Handle long-running extraction tasks via webhook callbacks instead of polling
- **Scalable Account Support**: Process invoices for 30+ accounts concurrently
- **FastAPI Backend**: Leverage async support and automatic Swagger documentation
- **Reliable Delivery**: Ensure no invoice is lost during the extraction and download pipeline

## 👤 User Stories

- As a **finance team member**, I want invoices extracted automatically so I can focus on analysis instead of manual retrieval
- As an **operations analyst**, I want daily invoice data available without manual intervention so I can generate timely reports
- As a **system operator**, I want webhook notifications so I don't need to poll for extraction status
- As a **developer**, I want automatic Swagger docs so I can easily test and understand the API

## 🔄 Extraction Flow

```text
1. Scheduler triggers extraction request
   ↓
2. FastAPI submits CFDI extraction request to SAT.ws API
   ↓
3. SAT.ws processes the request asynchronously
   ↓
4. SAT.ws sends webhook notification to FastAPI endpoint
   ↓
5. Webhook handler verifies notification and fetches invoice status
   ↓
6. FastAPI downloads XML and PDF files from SAT.ws
   ↓
7. Files are stored and made available for downstream consumption
```

## 🧱 Core Components

### FastAPI Application

- **Extraction Endpoint**: Accepts account credentials and CFDI parameters, submits extraction request to SAT.ws
- **Webhook Endpoint**: Receives async notifications from SAT.ws when invoices are ready for download
- **Download Service**: Fetches XML and PDF files from SAT.ws after notification
- **Scheduler**: Triggers periodic extraction for all configured accounts

### SAT.ws Integration

- **Authentication**: API key-based authentication with SAT.ws
- **Extraction Request**: POST request with account credentials and date range
- **Webhook Registration**: Configurable callback URL for async notifications
- **File Download**: GET request to retrieve XML and PDF invoices

### Data Storage

- **Invoice Metadata**: Account ID, extraction date, invoice count, processing status
- **File Storage**: Downloaded XML and PDF files organized by account and date

## 📚 References

- [SAT.ws API Documentation](https://sat.ws)
- [Architecture Diagram](./diagram.puml)