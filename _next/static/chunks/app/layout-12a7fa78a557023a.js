(self.webpackChunk_N_E = self.webpackChunk_N_E || []).push([[185], {
    6974: function(e, o, r) {
        Promise.resolve().then(r.bind(r, 0)),
        Promise.resolve().then(r.t.bind(r, 2853, 23)),
        Promise.resolve().then(r.t.bind(r, 4752, 23))
    },
    0: function(e, o, r) {
        "use strict";
        r.r(o);
        var t = r(7437);
        o.default = ()=>(0,
        t.jsx)("footer", {
            children: "Celebratory Technology - Disco Ball"
        })
    },
    2853: function() {},
    4752: function(e) {
        e.exports = {
            style: {
                fontFamily: "'__Roboto_6cc195', '__Roboto_Fallback_6cc195'",
                fontStyle: "normal"
            },
            className: "__className_6cc195"
        }
    },
    622: function(e, o, r) {
        "use strict";
        /**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Meta Platforms, Inc. and affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
        var t = r(2265)
          , n = Symbol.for("react.element")
          , s = (Symbol.for("react.fragment"),
        Object.prototype.hasOwnProperty)
          , c = t.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner
          , _ = {
            key: !0,
            ref: !0,
            __self: !0,
            __source: !0
        };
        function q(e, o, r) {
            var t, l = {}, f = null, i = null;
            for (t in void 0 !== r && (f = "" + r),
            void 0 !== o.key && (f = "" + o.key),
            void 0 !== o.ref && (i = o.ref),
            o)
                s.call(o, t) && !_.hasOwnProperty(t) && (l[t] = o[t]);
            if (e && e.defaultProps)
                for (t in o = e.defaultProps)
                    void 0 === l[t] && (l[t] = o[t]);
            return {
                $$typeof: n,
                type: e,
                key: f,
                ref: i,
                props: l,
                _owner: c.current
            }
        }
        o.jsx = q,
        o.jsxs = q
    },
    7437: function(e, o, r) {
        "use strict";
        e.exports = r(622)
    }
}, function(e) {
    e.O(0, [971, 472, 744], function() {
        return e(e.s = 6974)
    }),
    _N_E = e.O()
}
]);
