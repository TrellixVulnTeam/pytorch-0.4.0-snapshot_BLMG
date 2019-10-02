/*
 * Copyright (c) 2017 ARM Limited.
 *
 * SPDX-License-Identifier: MIT
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to
 * deal in the Software without restriction, including without limitation the
 * rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
 * sell copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */
#ifndef ARM_COMPUTE_TEST_PRINTERS
#define ARM_COMPUTE_TEST_PRINTERS

#include "JSONPrinter.h"
#include "PrettyPrinter.h"

namespace arm_compute
{
namespace test
{
namespace framework
{
enum class LogFormat
{
    NONE,
    JSON,
    PRETTY
};

LogFormat log_format_from_name(const std::string &name);

inline ::std::stringstream &operator>>(::std::stringstream &stream, LogFormat &format)
{
    std::string value;
    stream >> value;
    format = log_format_from_name(value);
    return stream;
}

inline ::std::stringstream &operator<<(::std::stringstream &stream, LogFormat format)
{
    switch(format)
    {
        case LogFormat::PRETTY:
            stream << "PRETTY";
            break;
        case LogFormat::NONE:
            stream << "NONE";
            break;
        case LogFormat::JSON:
            stream << "JSON";
            break;
        default:
            throw std::invalid_argument("Unsupported log format");
    }

    return stream;
}
} // namespace framework
} // namespace test
} // namespace arm_compute
#endif /* ARM_COMPUTE_TEST_PRINTERS */
