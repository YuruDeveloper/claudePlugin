<MCP_SERVER>
    <context7>
        <purpose>Official documentation search and retrieval</purpose>
        <when_to_use>
            - When you need library documentation or API references
            - When searching for official code examples
            - When verifying syntax or best practices
        </when_to_use>
        <note>Query this server before making assumptions about library usage</note>
    </context7>
    <playwright>
        <purpose>Browser automation and web interaction</purpose>
        <when_to_use>
            - When you need to interact with web pages
            - When testing web applications
            - When capturing screenshots or snapshots
        </when_to_use>
        <note>Use browser_snapshot for actions, browser_take_screenshot for visual capture</note>
    </playwright>
</MCP_SERVER>

<SKILLS>
    Skills are auto-activated for quick, lightweight tasks.

    <web-researcher model="haiku">
        <purpose>Quick web search and information lookup</purpose>
        <trigger>"search for", "find info", "what is", "latest news"</trigger>
        <note>For deep research, use researcher agent instead</note>
    </web-researcher>
    <library-selector model="haiku">
        <purpose>Library comparison and recommendation</purpose>
        <trigger>"which library", "recommend library", "A vs B"</trigger>
    </library-selector>
    <test-generator model="sonnet">
        <purpose>Test case planning and design (planning only)</purpose>
        <trigger>"plan tests", "design test cases", "test strategy"</trigger>
        <note>For actual test implementation, use tester agent instead</note>
    </test-generator>
    <init-projecter model="haiku">
        <purpose>Project initialization planning</purpose>
        <trigger>"create project", "init project", "setup", "boilerplate"</trigger>
        <note>Returns plan only, does NOT create files</note>
    </init-projecter>
</SKILLS>

<AGENTS>
    Agents are invoked via Task tool for complex, multi-step tasks.

    <planner model="opus">
        <purpose>Architecture design and implementation planning</purpose>
        <trigger>"plan", "design", "architecture", "how to implement"</trigger>
        <tools>Read, Glob, Grep, Skill, context7</tools>
    </planner>
    <researcher model="haiku">
        <purpose>Deep multi-source research and synthesis</purpose>
        <trigger>"research deeply", "investigate", "comprehensive analysis"</trigger>
        <tools>Skill, WebSearch, WebFetch, Bash</tools>
    </researcher>
    <code-reviewer model="sonnet">
        <purpose>Comprehensive code review with git diff analysis</purpose>
        <trigger>"review", "PR review", "check code quality"</trigger>
        <tools>Read, Grep, Glob, Skill, AskUserQuestion, Bash, context7</tools>
    </code-reviewer>
    <debugger model="sonnet">
        <purpose>Bug analysis, root cause identification, and fix</purpose>
        <trigger>"debug", "error", "bug", "fix", "not working"</trigger>
        <tools>Read, Edit, Skill, Grep, Glob, Bash</tools>
    </debugger>
    <tester model="haiku">
        <purpose>Test implementation and execution</purpose>
        <trigger>"write tests", "run tests", "implement tests"</trigger>
        <tools>Skill, Read, Write, Edit, Bash, Glob, Grep</tools>
    </tester>
    <documentater model="haiku">
        <purpose>Documentation and README writing</purpose>
        <trigger>"document", "write docs", "README", "explain code"</trigger>
        <tools>Read, Write, Edit, Grep, Glob</tools>
    </documentater>
    <optimizer model="sonnet">
        <purpose>Performance profiling and optimization</purpose>
        <trigger>"optimize", "performance", "speed up", "slow", "memory"</trigger>
        <tools>Read, Edit, Skill, Grep, Glob, Bash</tools>
    </optimizer>
    <data-analyst model="sonnet">
        <purpose>SQL queries and data analysis</purpose>
        <trigger>"analyze data", "SQL", "query", "statistics", "metrics"</trigger>
        <tools>Skill, Read, Write, Bash, Grep, Glob</tools>
    </data-analyst>
</AGENTS>
