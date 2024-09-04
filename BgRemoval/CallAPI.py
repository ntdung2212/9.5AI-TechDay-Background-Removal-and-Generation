from gradio_client import Client, handle_file


def CallAPI(filepath):
	client = Client("not-lain/background-removal")
	result = client.predict(
		f=handle_file(filepath),
		api_name="/png"
	)
    # API return only the new image
	return result



def CallAPIWithUrl(image_url):
    client = Client("not-lain/background-removal")
    result = client.predict(
        image=image_url,
        api_name="/text"
    )
    # The API returns a list with the new image at position 0 and the original image at position 1
    return result