#!/bin/bash
curl --netrc-file ../.netrc -X POST https://community.cloud.databricks.com/api/2.0/clusters/create -H "Content-Type: application/json" -d @../clusters/my-sample-cluster.json
