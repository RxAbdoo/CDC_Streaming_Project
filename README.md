# CDC with Kafka KRaft, Debezium, Flink, and Postgres

## Overview

This project implements a robust **Change Data Capture (CDC)** pipeline leveraging the latest Kafka architecture with **Kafka KRaft** (ZooKeeper-less Kafka), **Debezium** as the CDC connector, **Apache Flink** for real-time stream processing, and **PostgreSQL** as the source database.

Here's how the data flows:

1. A Python script generates simulated financial transactions and inserts them into a PostgreSQL database.
2. **Debezium** monitors the PostgreSQL database’s transaction log and captures every change (inserts, updates, deletes) in real-time.
3. Debezium publishes these change events into Kafka topics managed by **Kafka KRaft**, eliminating the need for ZooKeeper and simplifying Kafka’s deployment and management.
4. **Apache Flink** consumes the Kafka topics, performing real-time stream processing, analytics, and transformations as required.

This architecture demonstrates a modern, scalable CDC pipeline suitable for development, testing, and as a foundation for production-ready streaming applications.

---

## Architecture Diagram

![System Architecture](CDC.png)

- **PostgreSQL**: Stores the source transaction data.
- **Debezium Connector**: Captures data changes from PostgreSQL WAL (Write-Ahead Log).
- **Kafka KRaft**: Kafka broker without ZooKeeper for managing topics and partitions.
- **Apache Flink**: Processes streaming data from Kafka topics in real-time.
- **Python Data Generator**: Simulates transaction inserts into PostgreSQL.

---

## Prerequisites

Make sure you have the following installed and configured before running the project:

- Python 3.9 or higher
- Docker and Docker Compose
- PostgreSQL database (local or remote)
- Python libraries:
  - `psycopg2-binary` (PostgreSQL adapter)
  - `faker` (data generation)
  - `apache-flink` (optional, for Flink API interaction)
- Basic familiarity with Kafka, Flink, Docker, PostgreSQL, and CDC concepts

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/RxAbdoo/CDC_Streaming_Project.git
cd CDC_Streaming_Project
