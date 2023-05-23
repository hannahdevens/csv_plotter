Rails.application.routes.draw do
  root 'csv_files#index'
  post '/create', to: 'csv_files#create'
end

