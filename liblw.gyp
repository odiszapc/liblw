{
    "target_defaults" : {
        "cflags" : [ "-Wall", "-std=c++11" ]
    },
    "targets" : [{
        "target_name" : "liblw",
        "type" : "shared_library",
        "include_dirs" : [ "./source" ],
        "cflags" : [ "-fPIC" ],
        "libraries" : [ "/usr/local/lib/libuv.a" ],
        "direct_dependent_settings" : {
            "include_dirs" : [ "./source" ],
            "libraries" : [ "-pthread" ]
        },
        "sources" : [
            "source/lw/Application.cpp",
            "source/lw/Application.hpp",
            "source/lw/Singleton.hpp",

            "source/lw/event/Loop.cpp",
            "source/lw/event/Loop.hpp"
        ]
    },{
        "target_name" : "libgtest",
        "type" : "static_library",
        "include_dirs" : [ "./gtest/include" ],
        "direct_dependent_settings" : {
            "include_dirs" : [ "./gtest/include" ]
        },
        "sources" : [ "gtest/fused-src/gtest/gtest-all.cc" ]
    },{
        "target_name" : "liblw-tests",
        "type" : "executable",
        "dependencies" : [ "liblw", "libgtest" ],
        "include_dirs" : [ "./tests" ],
        "sources" : [
            "tests/main.cpp"
        ]
    }]
}
