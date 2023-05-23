class CsvFilesController < ApplicationController
  def index
  end

  def create
    uploaded_file = params[:csv_file]
    file_path = Rails.root.join('public', 'uploads', uploaded_file.original_filename)

    File.open(file_path, 'wb') do |file|
      file.write(uploaded_file.read)
    end

    script_path = Rails.root.join('lib', 'scripts', 'plotter.py')

    system("python #{script_path} #{file_path}")

    @plot_path = '/uploads/plot.png'

    render 'create'
  end
end

