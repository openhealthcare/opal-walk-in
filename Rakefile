PROJ = "OPAL Walkin plugin"


task :pytest do
  p "Running Python Unit tests for #{PROJ}"
  sh "python runtests.py" do | ok, res |
    if not ok # Don't stacktrace please Rake. Ta.
      exit 1
    end
  end
end

task :devjstest do
  p "Running Javascript Unit tests for #{PROJ}"
  sh "export DISPLAY=:10; karma start config/karma.conf.developer.js --single-run" do | ok, res |
    if not ok # Don't stacktrace please Rake. Ta.
      exit 1
    end
  end
end

task :test => [:pytest, :jstest] do
  p "Run all tests"
end

task :devtest => [:pytest, :devjstest] do
  p "Run all development tests"
end  
