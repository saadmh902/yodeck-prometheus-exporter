# yodeck-prometheus-exporter
Export YoDeck Online/Offline status for use with prometheus/grafana


**Open yodeck-exporter.py add your API key and username**



**Add this into your prometheus config:**
<code>
  - job_name: "yodeck"
  - 
    static_configs:
    
      - targets: ["localhost:3304"]
    scrape_interval: 120s

    scrape_timeout: 40s
    
    metrics_path: /metrics
</code>

**Run yodeck-exporter.py**

**Launch Prometheus**

**Prometheus will now load data**
