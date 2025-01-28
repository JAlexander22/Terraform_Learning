#!/bin/bash
sudo yum update -y
sudo yum install -y curl wget git vim htop
sudo yum install -y httpd
sudo systemctl enable httpd
sudo systemctl start httpd