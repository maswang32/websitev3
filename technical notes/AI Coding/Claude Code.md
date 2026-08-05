- `claude "task"`  - run one time task
- `claude -p query` - run one time query
- `claude -c` continue most recent convo in the current directory
- `claude r` - resume a previous conversation
- `/clear` - clear conversation history
- `/help` - show available commands
- `/exit` - exit claude code
- `/resume` - resume an earlier session
- `claude --continue` - resume previous session

Shortcuts:
- / see all commands and skills
- Tab for command completion
- Up arrow for command history
- Shift+Tab to cycle permission modes

Tips:
- Be specific
- use step-by-step instructions
- let claude explore first


## Boris Cherny Talk
- works locally, remote ssh, tmux
- some anthropic employees always use IDE, but also use claude code inside it.

Useful:
1. /permissions - allow tools
2. /theme
3. /install-github-app
4. /config - turn on notifications
5. /terminal-setup - shift enter for newlines


### What to start with?
1. 2. No remote indexing, no training on generative models for the code
2. No setup
3. Codebase Q&A - start with this, ask questions about the codebase. onboarding takes 2-3 days
	1. It will find examples of usage for function calls
	2. ask it about git history
4. Practice prompting
	1. socratic prompting - don't be too sure of what you want it to do
	2. brainstorm, make a plan
5. Claude comes with 12 built in tools:
	1. bash, file search, file listing, file read and write, subagents, web fetch, search, subagents, TODOS
6. Plan:
	1. ask it to think first
	2. ask it to approve the plan
7. commit, push pr - auto PR
8. two kinds of tools:
	1. bash tools: 'use this CLI do do something'. it can also try using --help to figure out how to use it.
	2. MCP tools:
		1. tell it about MCP tools too
	3. you can give it all your tools
9. Common workflows:
	1. explore, plan, confirm, code, commit
	2. write tests, commit, code, iterate, commit
	3. write code, screenshot result, iterate
10. Checking work makes claude a lot more powerful - it can iterate. Iteration and feedback can make things perfect.
11. More context means better performance
	1. Claude.md
	2. Slash commands
	3. At-mentioning filenames (using @)
12. Claude.md - remember across sessions
	1. CLAUDE.md in the project root - automatically read into context, shared with team
	2. CLAUDE.local.md - not checked into source control
	3. keep claude files short, since they go into context, and it's usually not that useful
	4. should be common bash commands, style guide, MCP tools, architectural decisions, things that an employee would need to know.
	5. you can put claude.md in child directories that will get pulled in on command
13. how to pull in context?
	1. /user:foo --> ~./claude/commands/foo.md
	2. /project:foo --> .claude/commands/foo.md, in the project
		1. folder/ ---> @folder
			1. CLAUDE.md ---> pulled in automatically
			2. foo.py ---> /@:a:foo.py
			3. commands/foo.md --> /project:a:foo
14. .claude/commands
	1. slash commands
15. Take time to tune context
	1. prompt improver
	2. improves performance dramatically.
16. Context organization
	1. project (just me)
	2. global (just me)
	3. project (check in)
	4. global enterprise (everyone)
	5. Just me stuff:
		1. project:
			1. CLAUDE.local.md (just me)
			2. CLAUDE.md
			3. .claude/settings.local.json --- permissions (just me)_
			4. claude mcp --- mcp servers (just me)
			5. .mpc.json
			6. ./claude/settings.json
			7. ./claude/commmands
		2. global:
			1. ~/.claude.md (just me)
			2. ~/.claude/commands (just me)
			3. ~/.claude/settings.json (just me)
			4. claude mcp (just me)
		3. enterprise
			1. CLAUDE.md
			2. policies.json
17. /memory
	1. see all memory files getting pulled in
	2. you can edit memory files
18. configure claude MD, MCP servers, permissions, and slash commands for your team, and check them into git
19. keybindings
	1. shift tab to auto accept edits (bash commands still accepted).
		1. boris does this when it's on the right track
	2. # to create a memory
		1. tell it what to remember
	3. ! to enter bash mode
		1. also goes into the context window.
	4. @ to add a file or folder to context
	5. esc to cancel
		1. won't corrupt session or mess anything up, or corrupt
	6. esc x2 to jump back in history
	7. ctrl+r for verbose output (same thing in context window)
	8. /vibe
20. claude -p (SDK)
	1. programmatic, low level access to claude code
	2. automation, non-interactive tasks, building block for interactive apps
	3. supports CLI
	4. claude -p "what did I do this week?" ---output_format json --allowedTools.Bash(git log:*)
21. Multiclaude
	1. boris will have one claude running
	2. multiple checkouts in separate terminal tabs
	3. git worktrees
	4. tmux sessions into claude sessions
	5. github actions, launch jobs in parallel
22. images
	1. file path
	2. copy paste 
	3. drag and drop

### Q and A
1. why not IDE?
	1. don't waste time on UI, since people won't use IDEs soon
	2. people use different IDEs
2. 80% of techincal use claude code every day
3. researchers use the notebook tool