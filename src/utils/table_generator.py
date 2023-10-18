from src.utils.big_query import load_bq_config


class TableGenerator:
    def __init__(self, path):
        self.ddl = self.read_ddl_from_path(path=path)
        self.credentials, self.client, self.bq_project = load_bq_config()

    @staticmethod
    def read_ddl_from_path(path):
        with open(path, "r") as file:
            ddl = file.read()
        return ddl

    def create_table(self):
        query = self.ddl
        table = self.client.query(query=query, project=self.bq_project)
        return table.destination.project, table.destination.dataset_id, table.destination.table_id

    def delete_table(self, table):
        query = f"DROP TABLE {table};"
        jop = self.client.query(query=query, project=self.bq_project)
        jop.result()

