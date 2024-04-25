# yodeck-prometheus-exporter
Export YoDeck Online/Offline status for use with prometheus/grafana


Open yodeck-exporter.py add your API key and username

run yodeck-exporter.py

Add this into your prometheus config:

  - job_name: "yodeck"
  - 
    static_configs:
    
      - targets: ["localhost:3304"]
      - 
    scrape_interval: 120s

    scrape_timeout: 40s
    
    metrics_path: /metrics
    

Prometheus will now load data
