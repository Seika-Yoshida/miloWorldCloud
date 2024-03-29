import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
from wordcloud import WordCloud

WORD = """
As the afternoon sun filters through the window, casting warm, dancing patterns on the floor,
I find myself in a contemplative mood, stretched out comfortably on my favorite spot. The house is quiet,
a rare but peaceful interlude in our usually bustling home. My ears perk up at the faint,
familiar sounds of life around me—the distant hum of the slow cooker promising another culinary delight,
the soft rustle of leaves outside as the wind whispers secrets to them. In these moments,
I feel an overwhelming sense of contentment, a testament to the love and security that envelops me like a warm blanket.
My thoughts wander to the adventures that await me. The park, with its myriad smells and sights,
calls to me. I dream of chasing after my ball with reckless abandon, the grass beneath my paws,
the wind in my face. Yet, it's not just the thrill of the chase or the joy of the catch that fills me with anticipation;
it's the shared laughter, the looks of affection, and the bond that strengthens with every throw and fetch.
These experiences, simple yet profound, are the threads that weave the rich tapestry of my life with my family.
But beyond the play and companionship, there's a deeper, quieter reflection within me—a gratitude for the life I lead.
From the care taken in preparing my meals to the gentle touch that soothes me to sleep each night, every action speaks of love.
As I drift off into a gentle nap, lulled by the serenity of my surroundings, I can't help but feel fortunate. In the grand scheme of things,
I'm just a small part of this world, yet to my family, I'm a world of my own. And for that, my heart is full.
"""
IMAGE_MASK_PATH = "./milo_mask.png"

alice_mask = np.array(Image.open(IMAGE_MASK_PATH))

# WordCloud
word_cloud = WordCloud(
    background_color="white",
    mask=alice_mask,
    width=800, 
    height=800 
)
word_cloud.generate(WORD)

plt.figure(figsize=(10, 10)) 
plt.imshow(word_cloud, interpolation="bilinear")
plt.axis("off")

plt.savefig("./milo_high_res.png", dpi=300)

plt.show()