import clickhouse_connect

client = clickhouse_connect.get_client(
    host='lp2qum9z4z.ap-south-1.aws.clickhouse.cloud',
    user='default',
    password='JB0dE9p4lCX_z',
    secure=True
)

# Check available tables
result = client.query("SHOW TABLES")

print("Available Tables:")
for row in result.result_rows:
    print(row[0])