import parser


class TestSuite():
    def test_iperf3_client_connection(self, client):
        transfer_expected = 2
        bitrate_expected = 20

        transfer_criteria = lambda result: result['Transfer'] >= transfer_expected
        bitrate_criteria = lambda result: result['Bitrate'] >= bitrate_expected

        output, error = client

        if error:
            assert False, f"Client error: {error}"

        results = parser.parse(output)

        if not results:
            assert False, f"Error, no client output"

        if not any(transfer_criteria(result) for result in results):
            assert False, f"Error, transfer is lower than expected. Transfer values < {transfer_expected}"

        if not any(bitrate_criteria(result) for result in results):
            assert False, f"Error, bitrate is lower than expected. Bitrate values < {bitrate_expected}"

        assert True
