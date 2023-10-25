from telethon import TelegramClient, events
import telebot
from telebot.types import InlineKeyboardMarkup
from telebot.types import InlineKeyboardButton
import requests
import asyncio
import time
import random
import json
import re

Api_id = 26809799
Api_hash = '025028d3ce9bfe5c7f9fd2b6a6185290'

client = TelegramClient('anon', Api_id, Api_hash)
client.parse_mode = 'html'

Token = '6568063868:AAH6Gvkmk7MxoqzRTizu48b0yttVyRzZKbs'

Id_channel = '-1001841182626'

bot = telebot.TeleBot(Token, parse_mode='html')
 
chats = [
'@JulietteCheckerBot',
'@YoimiyaChkBot',
'@RickPrimeChkBot',
'@CuartelCardingGrupo',
'@freeusersdev',
'@RemChatChk',
'@AlisaCheckerChat',
'@tokyobinschat2',
'@Venexchk',
'@PoseidonAccts_chat',
'@NagisaChkFree',
'@ScrapperLala',
'@LalaScrapperFree',
'@alterchkchat',
'@sanjichk',
'@DeltaAccChat',
'@expropia2',
'@AssociatonBinners1',
'@+ZJ1ETs_wK6o1OTI0',
'@savagegroupoficial',
'@BinsHellChat',
'@rigbyfree',
'@TechzillaChkChat',
'@bcycc',
'@carol5auth',
'@ChkBotLand',
'@DarksideGrChat',
'@BINSSDARKGT',
'@AquachkFree',
'@TeamCreditCcard',
'@arkhamgroup',
'@TohruScrapperFree',
'@NiniCheckerChat',
'@AlisaCheckerChat',
'@AlisaChks',
'@accerroreschecker',
'@OficialScorpionsGrupo',
'@DrolyChatx',
'@alterchkchat',
'@BinsHellChat',
'@NiniCheckerChat',
'@NagisaChkFree',
'@ChkBotLand',
'@secretgroup01',
'@akatsukichks',
'@BINSSDARKGT',
'@expropia2',
'@CuartelCardingGrupo',
'@dSnowChat',
'@freeusersdev',
'@TechzillaChkChat',
'@CHECKEREstefany_bot',
'@astachkccs',
'@AlisaCheckerChat',
'@ritagroupOfc',
'@KobyChkFree',
'@Free_Ishtachk'
]

keywords = [
    'APPROVED',
    "CCN Error: Your card's security code is incorrect.",
    'Approved',
    '✅✅✅ Approved ✅✅✅',
    "Approved",
    "Succeeded! 🤑",
    "APPROVED",
    "APPROVED ✅",
    "✅✅✅ Approved ✅✅✅",
    "Approved CCN",
    "Approved #AUTH! ✅",
    "Approved ❇️",
    "APPROVED ✅",
    "APPROVED ✓",
    "✅Appr0ved",
    "Security code incorrect✅",
    "Approved ❇️",
    "CVV2 FAILURE POSSIBLE CVV ⌯ N - AVS: G",
    "Succeeded!",
    "𝑨𝒑𝒑𝒓𝒐𝒗𝒆𝒅 𝑪𝒂𝒓𝒅 ✅",
    "𝑨𝒑𝒑𝒓𝒐𝒗𝒆𝒅",
    "𝑪𝒉𝒂𝒓𝒈𝒆𝒅 𝟎.𝟐𝟓$",
    "𝑪𝒉𝒂𝒓𝒈𝒆𝒅 $3 ✅",
    "Succeeded",
    "Error: Your card has insufficient funds.",
    "Subscription complete",
    "CVV LIVE ✅",
    "Card Approved CCN/CCV Live",
    "incorrect_cvc",
    "Dev:",
    "APPROVED ✓",
    "1000: Approved",
    "𝑨𝑷𝑷𝑹𝑶𝑽𝑬𝑫",
    "Payment failed! (N7: Decline for CVV2 failure)",
    "avs: Gateway Rejected: avs",
    "CVV2/VAK Failure",
    "CVV2 MISMATCH Approved! ✅",
    "Aprobada ✅",
    "Gateway Rejected: avs_and_cvv",
    "Gateway Rejected: avs",
    "CVC Declined",
    "★LIVE CVV★",
    "CCN CARD / 2010 Card Issuer Declined CVV",
    "★LIVE CNN★",
    "CCN Card! ✅",
    "1000 Approved",
    "Approved CCN",
    "2010 Card Issuer Declined CVV",
    "Card Issuer Declined CVV",
    "Added to free trial",
    "Gateway Rejected: avs (1000)",
    "CVV.",
    "Approved (1000)",
    "Approved 🟩",
    "Security code incorrect✅",
    "[ APPROVED ✅ ]",
    "Approved! ✅",
    "Approved ❇️",
    "✅Approved",
    "AUTHORIZED",
    "CVV2 Mismatch: 15004-This transaction cannot be processed. Please enter a valid Credit Card Verification Number.",
    "E00027: The transaction has been declined because of an AVS mismatch. The address provided does not match billing address of cardholder.",
    "CCN CARD / CVV2 Mismatch: 15004-This transaction cannot be processed. Please enter a valid Credit Card Verification Number.",
    "Insufficient Funds Failed"
]

sent_cards = set()

async def format_card_message(text):
    card_info = re.search(r'(\d{16}\|\d{2}\|\d{4}\|\d{3})', text)
    if card_info:
        card_number = card_info.group(1)
        formatted_text = text.replace(card_number, f"<code>{card_number}</code>")
        return formatted_text

@client.on(events.MessageEdited)
async def event_handler(event):
    text = event.raw_text

    if any(keyword in text for keyword in keywords) and text not in sent_cards:
        sent_cards.add(text)
        formatted_message = await format_card_message(text)
        

        if formatted_message:
            bot.send_message(Id_channel,formatted_message, parse_mode="HTML")
            

client.start()
client.run_until_disconnected()