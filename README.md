# IAP Sample App

Displays the email address of the logged in user from the value of the `x-goog-authenticated-user-email` header inserted by the Identity-Aware Proxy.

## Building

```
gcloud container builds submit --project cloud-solutions-group --config cloudbuild.yaml .
```

## Running

Run on GKE:

```
# Set ENDPOINT_URL to the address routed through IAP. This can be a Cloud Endpoints URL like the example below.
ENDPOINT_URL=esp-sample-app.endpoints.$(gcloud config get-value project).cloud.goog
cat deployment.yaml | sed -e "s/{{ENDPOINT}}/${ENDPOINT_URL}/" | kubectl apply -f -
```