# KafkaServer-Python

Buiding a **[Kafka](https://kafka.apache.org/)** server as a **microservice**, from an automated **containerized** implementation in **[AWS EC2](https://aws.amazon.com/console/)** and use **[Kafka-Python](https://pypi.org/project/kafka-python/)** consumer and producer in few simple steps!

## Kafka
Kafka is an **open source**, distributed, partitioned, fault-tolerant, and a horizontally scalable streaming platform used as a  **real-time publish-subscribe** messaging system. It persists data like a log aggregation and allows applications to push, pull, and process a continuous flow of data in real-time. It also supports strong recovery from failure mechanisms.

<img src="./Img/kafka.png"> <img src="./Img/kafkaPart.png">

## Kafka-Python
[Kafka-Python](https://pypi.org/project/kafka-python/) client is a Python implementation of the Apache Kafka distributed stream processing system with [KafkaConsumer](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaConsumer.html) (message consumer API) and [KafkaProducer](https://kafka-python.readthedocs.io/en/master/apidoc/KafkaProducer.html) (asynchronous message producer API) 

## Getting started with the setup

Launch an EC2 Instance using Ansible Playbook [yml](./aws-ec.yml). 
Requirements - Ansible, Python , Boto and an AWS Account to Launch an EC2 instance.

> **Note:** [Ansible](https://docs.ansible.com) automation engine will be used for [AWS EC2](https://aws.amazon.com/console/) provisioning and application deployment. Install Ansible for Mac (using Homebrew or Python pip Package Manager).

    brew install ansible      
or

    pip3 install ansible  

>  Install Boto with pip, ([Boto](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) is the Amazon Web Services (AWS) SDK for Python)

    pip3 install boto

>  Create a .boto file with the AWS account credentials in credentials.csv and save with permission 400 -> chmod 400 .boto so that, (U)ser / owner can read, can't write and can't execute

    [Credentials]
    aws_access_key_id = [Access key ID]
    aws_secret_access_key = [Secret access key]

> Run the playbook - 

    ansible-playbook aws-ec.yml


pip3 install kafka-python
