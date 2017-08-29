# Changelog
## [v0.1.0](https://github.com/aemx/geweva/tree/0.1.0) (2017-08-29)

[Full Changelog](https://github.com/aemx/geweva/compare/0.0.3...0.1.0)

**Additions:**

- A `logs/` folder is now used for storing all logs
    - _**Note:** Manual creation of a `logs/` folder is necessary for Geweva to run correctly.  
    This will become automatic by the first full release._

**Changes:**

- Logs are now stored as JSON files, rather than .log files
- Logs are now stored by week, in accordance with ISO 8601

**Removed:**

- Support for previously used .log files

## [v0.0.3](https://github.com/aemx/geweva/tree/0.0.3) (2017-08-25)

[Full Changelog](https://github.com/aemx/geweva/compare/0.0.2...0.0.3)

**Changes:**

- Moving average is now calculated as a sinusoidal function fit to a linear trendline
    - _**Note:** This may change to a sinusoidal-polynomial in the future_

## [v0.0.2](https://github.com/aemx/geweva/tree/0.0.2) (2017-08-25)

[Full Changelog](https://github.com/aemx/geweva/compare/0.0.1...0.0.2)

**Additions:**

- `src/` folder created for scripts executed from the main script

**Changes:**

- The plotter and file handler are now standalone scripts
- Code cleanup

**Fixes:**

- Returning to the main script now includes the list of operations

## [v0.0.1](https://github.com/aemx/geweva/tree/0.0.1) (2017-08-24)

**Additions:**

- While statements to input segments
- Log creation prompt
- Changelog
- Git ignore file
- License file

**Changes:**

- Typing effect speed increased
- Appropriate concision edits