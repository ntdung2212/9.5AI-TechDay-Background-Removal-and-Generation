from gradio_client import Client, handle_file


def CallAPI(filepath):
	client = Client("not-lain/background-removal")
	result = client.predict(
		f=handle_file(filepath),
		api_name="/png"
	)
	return result