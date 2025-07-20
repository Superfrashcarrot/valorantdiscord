import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="", intents=intents)

@bot.event
async def on_ready():
    print(f'✅ 로그인됨: {bot.user}')

    try:
        guild = discord.Object(id=1114053329190924399)  # ✅ 서버 ID 교체 가능
        synced = await bot.tree.sync(guild=guild)        # 슬래시 명령어 동기화
        print(f"🛠️ {guild.id} 서버에 명령어 {len(synced)}개 동기화 완료")
    except Exception as e:
        print(f"⚠️ 명령어 동기화 중 오류 발생: {e}")

@bot.tree.command(name="맵선택", description="맵과 사이트를 선택해 관련 채널로 안내합니다.")
async def select(interaction: discord.Interaction, 맵: str, 사이트: str):
    키 = f"{맵}_{사이트.lower()}"
    print(f"입력된 키: {키}")

    채널매핑 = {
        "아이스박스_a": 1394514409560211527,
        "바인드_b": 1395096099600994324,
        "헤이븐_c": 1393992024478187520
    }

    if 키 in 채널매핑:
        채널 = bot.get_channel(채널매핑[키])
        await interaction.response.send_message(
            f"{interaction.user.mention}님을 {채널.mention}로 안내합니다! ✨"
        )
    else:
        await interaction.response.send_message("😅 해당하는 맵/사이트 채널이 없어요")

# 🔐 디스코드 봇 토큰 입력
bot.run("MTM5Mzk5MjAyNDQ3ODE4NzUyMA.GNiUvN.AdbSnIu2iZYKFedUw-36crszUNz6JqZmJGpoOk")