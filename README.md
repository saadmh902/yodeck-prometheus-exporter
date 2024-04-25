# yodeck-prometheus-exporter
Export YoDeck Online/Offline status for use with prometheus/grafana


**Open yodeck-exporter.py add your API key and username**



**Add this into your prometheus config:**
```
  - job_name: "yodeck"
    static_configs:
      - targets: ["localhost:3304"]
    scrape_interval: 120s
    scrape_timeout: 40s
    metrics_path: /metrics
```

**Run yodeck-exporter.py**

**Launch Prometheus**

**Prometheus will now load data**


# Examples of final product:

**Exporter running**
![image](https://github.com/saadmh902/yodeck-prometheus-exporter/assets/49423626/3f1b679a-06ee-4827-ae8c-ed79618cde9a)

**Grafana Example**
![image](https://github.com/saadmh902/yodeck-prometheus-exporter/assets/49423626/9bd98f11-7462-49df-9329-0e1361f42b6c)

**Prometheus Scraping**
![image](https://github.com/saadmh902/yodeck-prometheus-exporter/assets/49423626/1a9d1f37-c16b-4284-b81c-d3cd0d4227a1)
