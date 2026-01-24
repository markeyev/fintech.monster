#!/bin/bash
# Deploy to Google Cloud Storage
# Usage: ./deploy.sh [BUCKET_NAME]

BUCKET_NAME=${1:-fintech-monster-regional}

echo "Building production site..."
make publish

echo "Deploying to gs://$BUCKET_NAME..."

# Requires Google Cloud SDK (gcloud) to be installed and authenticated
# gcloud auth login
# gcloud config set project [YOUR_PROJECT_ID]

# Command to sync the output directory with the GCS bucket
# -r: recursive
# -d: delete extra files in destination (mirror)
# gcloud storage rsync -r output gs://$BUCKET_NAME

echo "SUCCESS: Build complete. To deploy, ensure GCS bucket '$BUCKET_NAME' exists and run:"
echo "gcloud storage rsync -r output gs://$BUCKET_NAME"
