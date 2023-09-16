# OpenWeatherETL
## 專案說明
### 專案名稱: 利用AWS建立Open Weather ETL 並整合至 Apache Airflow
**詳情請參閱[openweatherETL.pdf](https://github.com/jerry7776112/openweatherETL/blob/main/openweatherETL.pdf)**
### 實作說明
##### 利用AWS開發自動化抓取OpenWeather天氣資訊的ETL
* 建立 AWS EC2 並整合至 Local端 Virtual Studio Code 編譯
* Apache Airflow 端口設定
* 建立 AWS S3
* 整合ETL至Apache Airflow 
* 遇到Error設定EC2及S3 的IAM policy
* 修正error重新執行ETL 

### Flow
![flowchart](https://github.com/jerry7776112/openweatherETL/blob/main/flow/openweatherETLflow.png "flowchart")

### 實務知識
* Python
* Apache Airflow
* AWS EC2 建立
* AWS S3 建立
* AWS port 設定
* AWS security policy 設定
* 利用 AWS 建立 ETL
* 將AWS EC2 整合到 Local端 Visual Studio Code編譯

### 前置準備
* 註冊open_weather帳號獲得API Keys
<https://openweathermap.org/>
* 註冊AWS 帳號
<https://aws.amazon.com/tw/>
* 建立一個 EC2(建立EC2教學內容於**openweatherETL.pdf**中)
* **AWS EC2 Ubuntu需安裝的套件**
  ```
  sudo apt update
  ```
  ```
  sudo apt install python3-pip
  ```
  ```
  sudo pip install pandas
  ```
  ```
  sudo pip install s3fs
  ```
  ```
  sudo pip install apache-airflow
  ```
  ```
  sudo pip install requests
  ```
