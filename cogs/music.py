import typing
import logging
import discord
from discord.ext import commands
import wavelink

class Music(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.lavalink_nodes = [
            {"uri": "https://v4.lavalink.rocks:443", "password": "horizxon.tech"},
            # {"uri": "https://lavalink-v4.huntools-bot.xyz:443", "password": "youshallnotpass"},
            # {"uri": "https://lava-v4.ajieblogs.eu.org:443", "password": "https://dsc.gg/ajidevserver"},
            # {"uri": "https://lavalinkv4-eu.serenetia.com:443", "password": "BatuManaBisa"},
            # {"uri": "https://lavalink.hewkawar.xyz:443", "password": "HewkawArPass"},
            # {"uri": "http://lavalink.jompo.cloud:2333", "password": "jompo"},
            # {"uri": "http://ll.sleepyinsomniac.eu.org:80", "password": "youshallnotpass"},
            # {"uri": "http://buses.sleepyinsomniac.eu.org:80", "password": "youshallnotpass"},
            # {"uri": "http://node.lewdhutao.my.eu.org:80", "password": "youshallnotpass"},
            # {"uri": "http://ether.lunarnodes.xyz:6969", "password": "lunarnodes.xyz"},
            # {"uri": "http://lavalink.jirayu.net:13592", "password": "youshallnotpass"},
            # {"uri": "http://lavalink01.techbyte.host:2036", "password": "NAIGLAVA-dash.techbyte.host"},
            # {"uri": "http://lava-v4.ajieblogs.eu.org:80", "password": "https://dsc.gg/ajidevserver"},
            # {"uri": "http://lavalink1.albinhakanson.se:1141", "password": "albinhakanson.se"},
            # {"uri": "http://nyc01.jxshua.dev:4000", "password": "youshallnotpass"},
            # {"uri": "http://lavalinkv4-id.serenetia.com:80", "password": "BatuManaBisa"},
            # {"uri": "http://lavalinkv4-eu.serenetia.com:80", "password": "BatuManaBisa"},
            # {"uri": "http://lavalink.clxud.dev:2333", "password": "youshallnotpass"},
            # {"uri": "http://37.27.114.136:25065", "password": "reedrouxfreenode"},
            # {"uri": "http://lavalink4.theelf.tech:25577", "password": "https://dsc.gg/elfmusic"},
            # {"uri": "http://v4.lavalink.rocks:80", "password": "horizxon.tech"},
            # {"uri": "http://lava.catfein.com:5000", "password": "catfein"}
        ]
        self.bot.loop.create_task(self.startNodes())

    async def startNodes(self):
        await self.bot.wait_until_ready()
        nodes = []
        for node in self.lavalink_nodes:
            try:
                node = wavelink.Node(
                    client=self.bot,
                    **node
                )
                nodes.append(node)
                print(f"Created wavelink node: {node.identifier}")
            except Exception as e:
                print(f"Exception occured while creating wavelink node{node['uri']}:{node['port']} \n{e}")
        try:
            await wavelink.Pool.connect(nodes=nodes, client=self.bot)
            print(f"Wavelink Pool Creation Successful.")
        except Exception as e:
            print(f"Exception occured while creating wavelink node pool. \n{e}")
    
    async def getNodes(self):
        return sorted(wavelink.Pool.nodes.values(), key=lambda n: len(n.players))

    async def stopNodes(self):
        try:
            await wavelink.Pool.close()
            print("Closed all nodes in the pool.")
        except Exception as e:
            print(f"Exception occurred while closing wavelink node pool. \n{e}")

    async def on_wavelink_node_ready(self, payload: wavelink.NodeReadyEventPayload) -> None:
        logging.info("Wavelink Node connected: %r | Resumed: %s", payload.node, payload.resumed)

    async def on_wavelink_track_start(self, payload: wavelink.TrackStartEventPayload) -> None:
        player: wavelink.Player | None = payload.player
        if not player:
            return

        original: wavelink.Playable | None = payload.original
        track: wavelink.Playable = payload.track

        embed: discord.Embed = discord.Embed(title="Now Playing")
        embed.description = f"**{track.title}** by `{track.author}`"

        if track.artwork:
            embed.set_image(url=track.artwork)

        if original and original.recommended:
            embed.description += f"\n\n`This track was recommended via {track.source}`"

        if track.album.name:
            embed.add_field(name="Album", value=track.album.name)

        await player.home.send(embed=embed)

    @commands.hybrid_command(name='play', description="Make the bot join the channel.")
    async def play(self, ctx: commands.Context, *, query: str):
        if not ctx.guild:
            return

        player: wavelink.Player
        player = typing.cast(wavelink.Player, ctx.voice_client)  # type: ignore

        if not player:
            try:
                player = await ctx.author.voice.channel.connect(cls=wavelink.Player)  # type: ignore
            except AttributeError:
                await ctx.send("Please join a voice channel first before using this command.")
                return
            except discord.ClientException:
                await ctx.send("I was unable to join this voice channel. Please try again.")
                return

        player.autoplay = wavelink.AutoPlayMode.enabled

        if not hasattr(player, "home"):
            player.home = ctx.channel
        elif player.home != ctx.channel:
            await ctx.send(f"You can only play songs in {player.home.mention}, as the player has already started there.")
            return

        tracks: wavelink.Search = await wavelink.Playable.search(query)
        if not tracks:
            await ctx.send(f"{ctx.author.mention} - Could not find any tracks with that query. Please try again.")
            return
        
        if isinstance(tracks, wavelink.Playlist):
            # tracks is a playlist...
            added: int = await player.queue.put_wait(tracks)
            await ctx.send(f"Added the playlist **`{tracks.name}`** ({added} songs) to the queue.")
        else:
            track: wavelink.Playable = tracks[0]
            await player.queue.put_wait(track)
            await ctx.send(f"Added **`{track}`** to the queue.")

        if not player.playing:
            # Play now since we aren't playing anything...
            await player.play(player.queue.get())

        # Optionally delete the invokers message...
        try:
            await ctx.message.delete()
        except discord.HTTPException:
            pass

    @commands.hybrid_command(name='disconnect', description="Make the bot leave the channel.")
    async def disconnect(self, ctx: commands.Context):
        player: wavelink.Player = typing.cast(wavelink.Player, ctx.voice_client)
        if not player:
            return
        await player.disconnect()
        await ctx.message.add_reaction("\u2705")

async def setup(bot):
    await bot.add_cog(Music(bot))