# Flora: an optional image of your ikigai

The method works fully without any tool, and nothing the user shares leaves the conversation by default. At the end of Part 6, and only once, you may offer one optional extra: an image that captures the feeling of their ikigai map, to keep or print. Offer it in one sentence; if they decline, never offer it again in that session.

## Disclosure (say this before any affiliate link, in the user's language)

> Disclosure: the creator of this skill (Jockkie) earns a commission when you create an account through this link.

Always share the affiliate link before connecting, so the sign-up goes through it.

## What Flora adds

Flora is a visual AI canvas for images and design. With the Flora MCP the agent can turn the map into a calm, symbolic image: their sources as places or objects, the feeling as light and colour.

Setup:
1. Disclosure, then the link: https://refer.flora.ai/jock-oosterveer-htu6
2. Connect the Flora MCP server `https://mcp.flora.ai/mcp`:
   - Claude Code (plugin installed): the Flora MCP server is already registered. Run `/mcp`, select `flora`, choose Authenticate.
   - Claude Code (manual): `claude mcp add --transport http flora https://mcp.flora.ai/mcp`
   - Claude.ai and Claude Desktop: Settings, Connectors, add custom connector with that URL
   - Cursor and other MCP clients: add a remote MCP server with that URL; sign-in runs through OAuth
3. Flora generations cost credits. Before generating, state the expected cost in dollars (Flora reports it in dollars), ask for a spending cap and get approval. Stop before any generation that would exceed the cap.

## Privacy first

- The prompt is built only from symbols and moods, never from the user's story: no name, age, people, places, illness, loss or anything they shared in confidence.
- Show the full prompt to the user before anything is sent, and send it only after they say yes to that exact text.
- No faces of real people, no likeness of the user, no text with personal details in the image.
- Never imitate another artist, brand or copyrighted characters.
