#pragma once

#include "lw/event/Promise.hpp"
#include "lw/event/Promise.void.hpp"

namespace lw {
namespace event {

template< typename T >
inline Future< T > Promise< T >::future( void ){
    return Future< T >( m_state );
}

// -------------------------------------------------------------------------- //

inline Future< void > Promise< void >::future( void ){
    return Future< void >( m_state );
}

// -------------------------------------------------------------------------- //

template< typename T >
template< typename Func, typename >
Future<> Future< T >::then( Func&& func ){
    return then< void >( std::move( func ) );
}

template< typename T >
template<
    typename Func,
    typename FuncResult,
    typename std::enable_if< std::is_void< FuncResult >::value >::type*
>
Future<> Future< T >::then( Func&& func ){
    return then([ func ]( T&& value, Promise<>&& promise ){
        func( std::move( value ) );
        promise.resolve();
    });
}

}
}