import os
import pandas as pd
from django.shortcuts import render
from .forms import UploadFileForm
from django.core.files.storage import FileSystemStorage
import matplotlib
matplotlib.use('Agg')  # Use a non-interactive backend for matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import io
import urllib, base64

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            fs = FileSystemStorage()
            filename = fs.save(file.name, file)
            file_url = fs.url(filename)
            file_path = fs.path(filename)

            try:
                # process to upload csv file
                df = pd.read_csv(fs.path(filename))

                if df.empty:
                    raise ValueError("The uploaded CSV file is empty.")

                # Perform data analysis
                data_head = df.head().to_html()
                summary_stats = df.describe().to_html()

                # Identify missing values
                missing_values = df.isnull().sum().to_frame(name='Missing Values')
                missing_values = missing_values[missing_values['Missing Values'] > 0]
                missing_values = missing_values.to_html()

                # Handle missing values (example: fill with a default value or drop)
                df_filled = df.fillna(0)  # Filling missing values with 0
                # Alternatively, you could use df.dropna() to drop rows with missing values

                # Generate plots
                img = io.BytesIO()

                # Clear any existing plot to avoid mixing old and new plots
                plt.clf()

                sns.histplot(df.select_dtypes(include=['number']).iloc[:, 0]).get_figure().savefig(img, format='png')
                img.seek(0)
                plot_url = base64.b64encode(img.getvalue()).decode('utf-8')

                # Close the plot to release memory
                plt.close()

            except Exception as e:
                error_message = str(e)
                return render(request, 'upload.html', {'form': form, 'error': error_message})

            finally:
                # Clean up: delete the uploaded file
                if os.path.exists(file_path):
                    os.remove(file_path)

            return render(request, 'results.html', {
                'data_head': data_head,
                'summary_stats': summary_stats,
                'missing_values': missing_values,
                'plot_url': plot_url,
            })
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})