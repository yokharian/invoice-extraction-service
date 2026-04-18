# Invoice Extraction Service

![Architecture](http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.githubusercontent.com/yokharian/invoice-extraction-service/master/diagram.puml)

Automated CFDI invoice extraction from Mexico's SAT using FastAPI and webhook-based async processing.

## Tech Stack

- **Language**: Python
- **Framework**: FastAPI
- **External API**: [SAT.ws](https://sat.ws)
- **Pattern**: Webhook-based async pipeline

## How It Works

1. FastAPI submits CFDI extraction requests to SAT.ws for each account
2. SAT.ws processes the requests asynchronously in the background
3. When invoices are ready, SAT.ws sends a webhook notification
4. The webhook handler downloads XML and PDF files
5. Extracted invoices are stored for downstream consumption

## Features

- Async invoice extraction for 30+ accounts
- Webhook-based status notifications (no polling)
- Automatic XML and PDF file download
- FastAPI with Swagger UI for API exploration
- Scheduled extraction runs


## References

- [PRD](./prd.md)
- Blog post: [Invoice Extraction Automation](https://yokharian.dev/posts/invoice-extraction-automation)
