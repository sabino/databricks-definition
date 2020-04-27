Databricks Definition
--

### How to setup

This project relies entirely on `cluster-name` so we discourage you to use HARD links referencing to your cluster unless you never delete them.

Requirements:
 - Create a file called `config.json` and set either host, username and password like so:
 ```json
{
  "host": "community.cloud.databricks.com",
  "user": "your-user-email@example.com",
  "password": "It'sAsecr3t"
}
 ```

or set using a token (but note that some of future stuff might not work when using a Token):
 ```json
{
  "host": "community.cloud.databricks.com",
  "token": "your-user-email@example.com"
}
 ```

After that you can create a JSON file (there are two examples) inside the `clusters` directory.
And then just run it.

`python src/core.py`

### What is it doing currently?

- It lists all existing clusters and compares to the ones declared inside the `clusters` dir (comparing by the filename and the cluster_name).
- If there are any differences in something declared in the JSON file, it shows a differences and updates the cluster in Databricks.
- At the same time, it validated clusters that exist but have no declaration, and it shows a Warning.
- After that, it checks whether a declared cluster is in the Databricks, creating the cluster in case it is not there.

### Stuff that requires user/password instead of token:

If you don't really care about Permissions then you should use `token` but if you do care, since there is no way to set Permissions when using the Clusters API the workaround will be to login as the user and
make the requests using these internal endpoints:

- Login: `https://HOST.cloud.databricks.com/j_security_check`
- Set permissions: `https://HOST.cloud.databricks.com/acl/cluster/CLUSTER-ID`

While this might change in the future it is unlikely it changes for worst or that the refactor needed will be that difficult.
It is just a matter of intercepting the requests using a modern browser and recreating it using python.

### TODO:
- Refactor everything
  - The code is somewhat messy as I did this in one go without refactoring
  - Think functional (immutability)
- Update this README
- Add tests
