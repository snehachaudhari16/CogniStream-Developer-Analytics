import clickhouse_connect

if __name__ == '__main__':
    client = clickhouse_connect.get_client(
        host='lp2qum9z4z.ap-south-1.aws.clickhouse.cloud',
        user='default',
        password='JB0dE9p4lCX_z',
        secure=True
    )

    print("Result:", client.query("SELECT 1").result_set[0][0])