PROJ = "OPAL Walkin plugin"

task :devjstest do
  p "Running Javascript Unit tests for #{PROJ}"
  sh "export DISPLAY=:10; karma start config/karma.conf.developer.js --single-run" do | ok, res |
    if not ok # Don't stacktrace please Rake. Ta.
      exit 1
    end
  end
end
