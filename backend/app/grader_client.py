import httpx
import os


GRADER_URL = os.environ.get('GRADER_URL', 'http://grader:8080')


async def submit_run(language: str, code: str, tests: dict):
async with httpx.AsyncClient() as client:
res = await client.post(f"{GRADER_URL}/run", json={
'language': language,
'code': code,
'tests': tests,
}, timeout=60.0)
res.raise_for_status()
return res.json()
