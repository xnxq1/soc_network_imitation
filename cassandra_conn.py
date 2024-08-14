from cassandra import ConsistencyLevel
from cassandra.cluster import Cluster, ExecutionProfile, EXEC_PROFILE_DEFAULT
from cassandra.query import tuple_factory

profile = ExecutionProfile(
    consistency_level=ConsistencyLevel.LOCAL_ONE,
    serial_consistency_level=ConsistencyLevel.LOCAL_ONE,
    request_timeout=30,
    row_factory=tuple_factory
)
class Cassandra:
    def __init__(self, host: str='0.0.0.0', port: str='9042'):
        self.cluster = Cluster([host], port=port, execution_profiles={EXEC_PROFILE_DEFAULT: profile})

    def __aenter__(self):
        self.session = self.cluster.connect()

    def __aexit__(self, exc_type, exc_val, exc_tb):
        self.session.shutdown()


cassandra = Cassandra()
