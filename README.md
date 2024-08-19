# Provenance-Based Log Analysis

## Table of Contents

- [Overview](#overview)
- [Description](#project-description)
- [Problem Statement](#problem-statement)
- [Approach](#approach)
- [Objective](#objective)
- [Target Audience](#target-audience)
- [Installation & Usage](#installation--usage)
  - [Installation](#installation)
  - [Usage](#usage)
- [Results](#results)

## Overview

The "Provenance-Based Log Analysis" project leverages data provenance principles to scrutinize log data for potential malicious patterns. It employs a data flow model based on the `prov` Python library to establish a standard data flow structure. Subsequently, this project analyzes log files, generating a provenance model based on these logs. By comparing this log-derived model with the established default data flow, the project aims to detect and differentiate between legitimate and potentially malicious data flows.

## Project Description

### Problem Statement

In various systems and applications, it's crucial to ensure the integrity and legitimacy of data flows. Anomalies or malicious patterns within data flow can indicate potential security breaches or unauthorized activities. Traditional log analysis methods may lack comprehensive insights into the nature of data flow. By employing data provenance, this project seeks to provide a more robust and context-rich analysis of data movements.

### Approach

For demonstartion point of the tool is working on a hypthetical network model consists of a sesnor, controller and robotic arm which communicate on MQTT protocol as shown in below image.

![robotic_Arm](https://github.com/Ujjwal0919/Provenance-Builder/assets/45317789/e1ba12f1-1eaa-47ab-8bdc-629ab00f9732)



The tools work on the principle of Data Provenance which means any deviation from the normal data flow will flag the anamoly or malicious behaviour in data.

1. **Default Provenance Model**: The project starts by defining a standard or default data flow model using the `prov` library. This model represents an expected and legitimate flow of data within the system. User first can create a default provenance model which defined how the coming data is expected in the network. 


2. **Log-Based Provenance Model Generation**: Log files containing system or application activities are processed to create a provenance model specific to these logs. This model encapsulates the data flow derived solely from the observed log activities.

3. **Comparison and Analysis**: The generated log-based provenance model is then compared against the established default data flow model. Any discrepancies or differences between these models are investigated to determine if the observed data flow aligns with the expected behavior or deviates into potentially malicious patterns.

4. **Policy Check**: User can also create policies and then check if the coming data verifying the policies at each and every data point.

   ![Screenshot from 2023-12-07 14-25-40](https://github.com/Ujjwal0919/Provenance-Builder/assets/45317789/ca1043b9-8b60-41e2-96a7-e77b6f2ca6f8)


### Objective

The primary objective of the project is to enhance log analysis methodologies by incorporating data provenance principles. By examining the relationships and lineage of data movements within a system or application, the project aims to detect and flag any irregularities or malicious behaviors, providing insights for further investigation or preventative measures.

### Target Audience

- **Security Analysts**: To aid in the identification of potential security breaches based on data flow.
- **System Administrators**: To improve understanding and monitoring of data movements within systems.
- **Application Developers**: To implement enhanced data flow monitoring and security measures in their applications.


   


