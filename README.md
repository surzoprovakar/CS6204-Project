# 🔒 Improving Reliability for Distributed Data Replication

This project focuses on **ensuring trustworthy data replication** in distributed systems by integrating **Autonomous Trust Management (ATM)** and **Service Level Agreements (SLA)** directly into replicated data mechanisms.

By combining dynamic trust evaluation and formal reliability contracts, the system **enhances resistance to malicious data and unreliable nodes**, achieving a **21% improvement in system reliability**.

## Overview

Traditional replicated data systems assume that all replicas behave correctly — a risky assumption in adversarial or faulty environments.  
This project enhances replication trustworthiness by:

- Dynamically **evaluating node trustworthiness** through **Autonomous Trust Management (ATM)** models.
- Enforcing **Service Level Agreements (SLA)** for data availability, integrity, and latency.
- Actively **isolating malicious or underperforming replicas** based on trust and SLA violations.

## Key Features

- 🤖 **Autonomous Trust Management**: Continuously monitors and assesses node behavior without centralized control.
- 📜 **Service Level Agreements**: Defines clear contractual expectations for replication reliability.
- 🛡️ **Malicious Node Mitigation**: Reduces the impact of untrustworthy replicas dynamically.
- 📈 **Reliability Gains**: Improves overall system trustworthiness by **21%** compared to baseline replication protocols.

## Technologies Used

- **Go** — core distributed system and replication engine.
- **Python** — trust evaluation and monitoring modules.
- **JSON** — data interchange and trust metadata.

## Motivation

Modern distributed systems face threats from malicious insiders, network faults, and unpredictable node behavior.  
Simply replicating data without validating trust leads to vulnerabilities.  
This project builds a **self-managing, trust-aware** replication system that automatically adapts to maintain high reliability even under adverse conditions.

## Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/surzoprovakar/CS6204-Project.git
   cd CS6204-Project


## Installation
------------

To run the project, we need to install Python3, pip3, simpy, and pyCryptodome.
SimPy requires Python >= 3.6; both CPython and PyPy3 are known to work.
The following installation instructions are for Linux OS.

## Install Python3.10
- sudo apt update && sudo apt upgrade -y
- sudo apt install software-properties-common -y
- sudo add-apt-repository ppa:deadsnakes/ppa
- sudo apt install python3.10

## Install Pip3
sudo apt-get -y install python3-pip

## Install Simpy
pip3  install -U simpy

## Install PyCryptodome
pip3 install -U PyCryptodome 

## Run the Project in Linux
make

## Clean the Project in Linux
make clean
