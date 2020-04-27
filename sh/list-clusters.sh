#!/bin/bash
curl --netrc-file ../.netrc -X GET https://community.cloud.databricks.com/api/2.0/clusters/list
