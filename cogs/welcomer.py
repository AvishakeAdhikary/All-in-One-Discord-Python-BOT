import discord
from discord.ext import commands
from discord import File
import numpy as np
import cv2
import io
import requests
from PIL import Image as PILImage, ImageDraw, ImageFont
from settings import DISCORD_SERVER_WELCOME_CHANNEL_ID, DISCORD_BOT_COLOR_LIGHT, DISCORD_BOT_COLOR_EXTRA_2

class Welcomer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel_id = DISCORD_SERVER_WELCOME_CHANNEL_ID
        channel = self.bot.get_channel(channel_id)
        if channel is None:
            try:
                channel = await self.bot.fetch_channel(channel_id)
            except discord.NotFound:
                print(f"Channel with ID {channel_id} not found.")
                return
            except discord.Forbidden:
                print(f"Bot does not have permission to access channel with ID {channel_id}.")
                return
            except discord.HTTPException as e:
                print(f"HTTP Exception occurred: {e}")
                return
        print(f'Welcome Channel Name: {channel.name}')
        message = f'Welcome to {member.guild.name}'

        # Load background image
        background_image = cv2.imread("static/himym-umbrella.jpg")
        
        # Load user's profile image
        response = requests.get(str(member.avatar.url))
        user_profile_image = PILImage.open(io.BytesIO(response.content))
        user_profile_image = user_profile_image.resize((150, 150))
        
        # Create a circle mask for the profile picture
        circle_mask = np.zeros((150, 150), dtype=np.uint8)
        cv2.circle(circle_mask, (75, 75), 75, (255), thickness=-1)
        user_profile_image = np.array(user_profile_image.convert("RGBA"))
        user_profile_image[..., 3] = circle_mask
        
        # Convert user profile image to BGR format
        user_profile_image = cv2.cvtColor(user_profile_image, cv2.COLOR_RGBA2BGRA)
        
        # Define the position for the profile image on the background
        x_offset = 725
        y_offset = 100
        
        # Overlay the profile picture onto the background
        y1, y2 = y_offset, y_offset + user_profile_image.shape[0]
        x1, x2 = x_offset, x_offset + user_profile_image.shape[1]
        
        alpha_s = user_profile_image[:, :, 3] / 255.0
        alpha_l = 1.0 - alpha_s
        
        for c in range(0, 3):
            background_image[y1:y2, x1:x2, c] = (alpha_s * user_profile_image[:, :, c] + alpha_l * background_image[y1:y2, x1:x2, c])
        
        # Convert background image to PIL format for text drawing
        background_image_pil = PILImage.fromarray(cv2.cvtColor(background_image, cv2.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(background_image_pil)
        
        # Draw text
        font_path = "static/fonts/inter/Inter-VariableFont_opsz_wght.ttf"
        font = ImageFont.truetype(font_path, 50)
        
        # Calculate text size and position using bounding box
        def draw_centered_text(draw, text, position, font, fill):
            bbox = draw.textbbox((0, 0), text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            x, y = position
            draw.text((x - text_width / 2, y - text_height / 2), text, font=font, fill=fill)
        
        draw_centered_text(draw, message, (800, 400), font, DISCORD_BOT_COLOR_LIGHT)
        draw_centered_text(draw, f"@{member.name}", (800, 500), font, DISCORD_BOT_COLOR_EXTRA_2)
        
        # Save to file
        output = io.BytesIO()
        background_image_pil.save(output, format='JPEG')
        output.seek(0)
        
        file = File(fp=output, filename="welcome.jpg")
        await channel.send(f"Welcome, {member.mention}! SUIT UP!!!", file=file)
    
async def setup(bot):
    await bot.add_cog(Welcomer(bot))
