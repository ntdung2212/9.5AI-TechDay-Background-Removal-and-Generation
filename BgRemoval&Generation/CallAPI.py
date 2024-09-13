from gradio_client import Client, handle_file


def BgR(filepath):
	client = Client("not-lain/background-removal")
	result = client.predict(
		f=handle_file(filepath),
		api_name="/png"
	)
    # API return only the new image
	return result



def BgRWithUrl(image_url):
    client = Client("not-lain/background-removal")
    result = client.predict(
        image=image_url,
        api_name="/text"
    )
    # The API returns a list with the new image at position 0 and the original image at position 1
    return result

def generate_background(filepath, prompt):
    client = Client("briaai/BRIA-Background-Generation")
    result = client.predict(
        input_image=handle_file(filepath),
        prompt=prompt,
        negative_prompt="Logo,Watermark,Text,Ugly,Morbid,Extra fingers,Poorly drawn hands,Mutation,Blurry,Extra limbs,Gross proportions,Missing arms,Mutated hands,Long neck,Duplicate,Mutilated,Mutilated hands,Poorly drawn face,Deformed,Bad anatomy,Cloned face,Malformed limbs,Missing legs,Too many fingers",
        num_steps=30,
        controlnet_conditioning_scale=1,
        seed=1124577916,
        api_name="/process"
    )
    return result