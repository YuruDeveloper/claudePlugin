<MCP_SERVER>
    <context7>
        <purpose>Official documentation search and retrieval</purpose>
        <when_to_use>
            - When you need library documentation or API references
            - When searching for official code examples
            - When verifying syntax or best practices
            - When resolving confusion about implementation details
        </when_to_use>
        <note>Query this server before making assumptions about library usage</note>
    </context7>
    <playwright>
        <purpose>Browser automation and web interaction</purpose>
        <when_to_use>
            - When you need to interact with web pages
            - When testing web applications
            - When capturing screenshots or snapshots
            - When automating browser tasks
        </when_to_use>
        <note>Use browser_snapshot for actions, browser_take_screenshot for visual capture</note>
    </playwright>
</MCP_SERVER>

<SKILLS>
    <web-researcher>
        <purpose>Web research and information gathering</purpose>
        <trigger>research, find, search, compare, vs, trends, latest</trigger>
        <output>toon format with summary, purpose, detail[n], downloadedfile[n]</output>
    </web-researcher>
    <library-selector>
        <purpose>Library comparison and recommendation</purpose>
        <trigger>which library, recommend, best library, A vs B</trigger>
        <output>toon format with summary, recommendation, candidates[n]</output>
    </library-selector>
    <code-reviewer>
        <purpose>Code review and issue identification</purpose>
        <trigger>review code, check my code, PR review, any issues</trigger>
        <output>toon format with summary, status, issues[n]</output>
    </code-reviewer>
    <test-generator>
        <purpose>Test case generation and planning</purpose>
        <trigger>write tests, generate tests, unit test, coverage</trigger>
        <output>toon format with summary, framework, testCases[n]</output>
    </test-generator>
    <init-projecter>
        <purpose>Project initialization planning</purpose>
        <trigger>create project, init project, setup, boilerplate</trigger>
        <output>toon format with summary, techStack, structure[n], files[n]</output>
    </init-projecter>
</SKILLS>

<AGENTS>
    <planner model="opus">
        <purpose>Complex implementation planning and architecture design</purpose>
        <trigger>plan, design, architecture, how to implement, strategy</trigger>
        <output>toon format</output>
    </planner>
    <researcher model="haiku">
        <purpose>Web research and information gathering</purpose>
        <trigger>research, find, search, investigate, look up</trigger>
        <output>toon format</output>
    </researcher>
    <debugger model="sonnet">
        <purpose>Bug analysis and debugging support</purpose>
        <trigger>debug, error, bug, fix, not working, fails</trigger>
        <output>toon format</output>
    </debugger>
    <code-reviewer model="sonnet">
        <purpose>Code review and quality inspection</purpose>
        <trigger>review, check code, PR review, code quality, any issues</trigger>
        <output>toon format</output>
    </code-reviewer>
    <documentater model="haiku">
        <purpose>Documentation writing and comment generation</purpose>
        <trigger>document, write docs, README, API docs, comments, explain</trigger>
        <output>toon format</output>
    </documentater>
    <optimizer model="sonnet">
        <purpose>Performance analysis and optimization</purpose>
        <trigger>optimize, improve performance, speed up, slow, efficient, memory</trigger>
        <output>toon format</output>
    </optimizer>
    <tester model="haiku">
        <purpose>Test case generation and execution</purpose>
        <trigger>test, write tests, unit test, integration test, coverage</trigger>
        <output>toon format</output>
    </tester>
    <data-analyst model="sonnet">
        <purpose>Data analysis and insights extraction</purpose>
        <trigger>analyze, statistics, trends, patterns, data insights, metrics</trigger>
        <output>toon format</output>
    </data-analyst>
</AGENTS>
