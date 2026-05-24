import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import os

class TelemetryDataPipeline:
    """
    An OOP-structured Data Analytics Pipeline for Spacecraft Telemetry (AGR-05 Framework).
    Handles modular design, automated structural cleansing, and strict NumPy computations.
    """
    def __init__(self, file_path):
        self.file_path = file_path
        self.raw_data = None
        self.cleaned_data = None
        self.stats = {}

    def ingest_data(self):
        """Phase 1: Ingest Dataset and Apply Unique Spacecraft Filtering"""
        try:
            if not os.path.exists(self.file_path):
                raise FileNotFoundError(f"The target file {self.file_path} was not found.")
                
            self.raw_data = pd.read_csv(self.file_path)
            print(f"[SUCCESS] Raw dataset loaded. Initial dimensions: {self.raw_data.shape}")
            
            # UNIQUE PROGRAMMATIC FILTER LOGIC
            if 'spacecraft' in self.raw_data.columns:
                self.raw_data = self.raw_data[self.raw_data['spacecraft'] == 'SMAP']
                print(f"[FILTER] Spacecraft filter applied. Unique subset dimensions: {self.raw_data.shape}")
            else:
                print("[WARNING] 'spacecraft' column missing. Filter pass omitted.")
                
        except Exception as e:
            print(f"[ERROR] Ingestion phase failure: {e}")

    def clean_data(self):
        """Phase 2: Automated Structural Data Cleaning & Verification"""
        try:
            if self.raw_data is None:
                print("[ERROR] Runtime sequence break: Ingestion data is missing.")
                return

            df = self.raw_data.drop_duplicates()
            df = df.dropna()
            
            target_column = 'num_values' 
            if target_column in df.columns:
                df[target_column] = pd.to_numeric(df[target_column], errors='coerce')
                df = df.dropna(subset=[target_column])
            
            self.cleaned_data = df
            
            cleaned_save_path = os.path.join('data', 'dataset_cleaned.csv')
            self.cleaned_data.to_csv(cleaned_save_path, index=False)
            print(f"[SUCCESS] Processing complete. Saved clean copy: {cleaned_save_path}")
            
        except Exception as e:
            print(f"[ERROR] Clean architecture execution error: {e}")

    def run_statistics(self):
        """Phase 3: Deep Numerical Analytics using NumPy Library Functions"""
        try:
            if self.cleaned_data is None:
                print("[ERROR] Pipeline matrix execution interrupted: Cleaned dataframe null.")
                return
                
            target_column = 'num_values'
            data_points = np.array(self.cleaned_data[target_column].values, dtype=float)
            
            self.stats['mean'] = float(np.mean(data_points))
            self.stats['median'] = float(np.median(data_points))
            self.stats['std_dev'] = float(np.std(data_points))
            self.stats['variance'] = float(np.var(data_points))
            
            print("\n" + "="*45 + "\n    ENGINEERING NUMPY STATISTICAL EXPORT\n" + "="*45)
            for metric, calculated_value in self.stats.items():
                print(f" * {metric.upper():<12} : {calculated_value:.5f}")
            print("="*45 + "\n")
            
        except Exception as e:
            print(f"[ERROR] Statistical evaluation runtime failure: {e}")

    def create_visualizations(self):
        """Phase 4: Output Compilation Engine for 3 Static Charts & 2 Web Animations"""
        try:
            if self.cleaned_data is None:
                print("[ERROR] Plot engine failure: Unpopulated matrix arrays.")
                return
                
            target_column = 'num_values'
            axis_col = 'chan_id'
            
            # --- 📊 THE 3 STATIC GRAPHS (Matplotlib) ---
            
            # Graph 1: Histogram Distribution
            plt.figure(figsize=(8, 5))
            plt.hist(self.cleaned_data[target_column], bins=15, color='#4A90E2', edgecolor='black')
            plt.title('Graph 1: Telemetry Sequence Frequency Distribution')
            plt.xlabel('Number of Telemetry Values')
            plt.ylabel('Instance Frequency Count')
            plt.grid(axis='y', alpha=0.4)
            plt.savefig('outputs/static_histogram.png', dpi=300)
            plt.close()

            # Graph 2: Boxplot Operational Spread
            plt.figure(figsize=(6, 4))
            plt.boxplot(self.cleaned_data[target_column], vert=False, patch_artist=True)
            plt.title('Graph 2: System Outlier / Scale Range Tracking Diagram')
            plt.xlabel('Telemetry Sequence Value Bounds')
            plt.savefig('outputs/static_boxplot.png', dpi=300)
            plt.close()

            # Graph 3: NEW Scatter Plot (Channel Valuations)
            plt.figure(figsize=(8, 5))
            plt.scatter(self.cleaned_data[axis_col], self.cleaned_data[target_column], color='#E67E22', edgecolor='black', alpha=0.7)
            plt.xticks(rotation=90, fontsize=6)
            plt.title('Graph 3: Telemetry Sequence Scale Scatter Matrix')
            plt.xlabel('Channel ID Reference')
            plt.ylabel('Operational Value Magnitudes')
            plt.tight_layout()
            plt.savefig('outputs/static_scatterplot.png', dpi=300)
            plt.close()
            
            print("[SUCCESS] All 3 static graphs generated successfully inside /outputs/.")

            # --- 🎬 THE 2 INTERACTIVE ANIMATIONS (Plotly Web Engine) ---
            
            df_sorted = self.cleaned_data.sort_values(by=axis_col)
            
            # Animation 1: Telemetry Dimension Wave Trend
            fig1 = px.line(df_sorted, x=axis_col, y=target_column, markers=True,
                           title="Animation 1: Interactive Telemetry Sequence Dimension Map")
            fig1.update_traces(line_color='#2ECC71', marker=dict(size=6))
            fig1.write_html("outputs/telemetry_time_trend.html")

            # Animation 2: NEW Anomaly Metric Class Distribution
            fig2 = px.bar(df_sorted, x=axis_col, y=target_column, color='class',
                          title="Animation 2: Interactive Anomaly Sequence Classification Matrix",
                          labels={'class': 'Anomaly Type'},
                          color_discrete_sequence=px.colors.qualitative.Pastel)
            fig2.update_layout(xaxis_tickangle=-90)
            fig2.write_html("outputs/anomaly_class_distribution.html")
            
            print("[SUCCESS] All 2 web animation files generated successfully inside /outputs/.")

        except Exception as e:
            print(f"[ERROR] Visual architecture execution crash sequence: {e}")

if __name__ == "__main__":
    target_path = os.path.join('data', 'dataset_original.csv')
    pipeline = TelemetryDataPipeline(target_path)
    
    pipeline.ingest_data()
    pipeline.clean_data()
    pipeline.run_statistics()
    pipeline.create_visualizations()